import os
import json
import re
from datetime import datetime, timezone, timedelta
from googleapiclient.discovery import build
import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = "1ordgWcnAmJpxAVD8qXy0dXjhgqu5Y_g2LkJFnzxA9f0"
SHEET_TAB = "todos"
CHANNEL_HANDLES = [
    "FrierenManhwa1", "Manhwa_Fresh", "Manhwa_Teller1",
    "Magical_ManhwaRecaps", "MamoruManhwa", "TobsManhwa",
]
BACKFILL_DAYS = 305

HEADER = ["quero_postar", "obra", "canal", "data_postado", "viewers", "duracao", "link"]


def parse_duration(iso):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return ""
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return f"{h}:{mi:02d}:{s:02d}" if h else f"{mi}:{s:02d}"


def extract_video_id(url):
    m = re.search(r"(?:v=|youtu\.be/|shorts/)([A-Za-z0-9_-]{11})", url or "")
    return m.group(1) if m else None


def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
    yt = build("youtube", "v3", developerKey=os.environ["YOUTUBE_API_KEY"])
    creds = Credentials.from_service_account_info(
        json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    sheet = gspread.authorize(creds).open_by_key(SHEET_ID).worksheet(SHEET_TAB)

    rows = sheet.get_all_values()
    if not rows or rows[0] != HEADER:
        sheet.update([HEADER], "A1:G1")
        rows = sheet.get_all_values()

    existing_by_id = {}
    for i, row in enumerate(rows[1:], start=2):
        if len(row) >= 7:
            vid = extract_video_id(row[6])
            if vid:
                existing_by_id[vid] = i

    cutoff = datetime.now(timezone.utc) - timedelta(days=BACKFILL_DAYS)
    new_videos = []

    for handle in CHANNEL_HANDLES:
        resp = yt.channels().list(part="contentDetails,snippet", forHandle=handle).execute()
        if not resp.get("items"):
            print(f"channel not found: @{handle}")
            continue
        ch = resp["items"][0]
        uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]
        title = ch["snippet"]["title"]

        page_token = None
        stop = False
        while not stop:
            r = yt.playlistItems().list(
                part="contentDetails", playlistId=uploads,
                maxResults=50, pageToken=page_token,
            ).execute()
            for it in r["items"]:
                pub_str = it["contentDetails"].get("videoPublishedAt")
                if not pub_str:
                    continue
                pub = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
                if pub < cutoff:
                    stop = True
                    break
                vid = it["contentDetails"]["videoId"]
                if vid in existing_by_id:
                    continue
                new_videos.append({"id": vid, "channel": title, "published": pub})
            page_token = r.get("nextPageToken")
            if not page_token:
                break

    all_ids = [v["id"] for v in new_videos] + list(existing_by_id.keys())
    stats = {}
    for batch in chunk(all_ids, 50):
        r = yt.videos().list(part="statistics,contentDetails", id=",".join(batch)).execute()
        for it in r["items"]:
            stats[it["id"]] = {
                "views": int(it["statistics"].get("viewCount", 0)),
                "duration": parse_duration(it["contentDetails"]["duration"]),
            }

    new_rows = []
    for v in new_videos:
        s = stats.get(v["id"], {"views": 0, "duration": ""})
        new_rows.append([
            False, "", v["channel"],
            v["published"].strftime("%Y-%m-%d %H:%M"),
            s["views"], s["duration"],
            f"https://youtu.be/{v['id']}",
        ])
    if new_rows:
        sheet.append_rows(new_rows, value_input_option="USER_ENTERED")

    updates = []
    for vid, row_num in existing_by_id.items():
        if vid in stats:
            updates.append({"range": f"E{row_num}", "values": [[stats[vid]["views"]]]})
    if updates:
        sheet.batch_update(updates)

    print(f"added {len(new_rows)} new, updated {len(updates)} viewer counts")


if __name__ == "__main__":
    main()
