import os
import json
import re
from datetime import datetime, timezone, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = "1ordgWcnAmJpxAVD8qXy0dXjhgqu5Y_g2LkJFnzxA9f0"
SHEET_TAB = "todos"
CHANNEL_HANDLES = [
    "FrierenManhwa1", "Manhwa_Fresh", "Manhwa_Teller1",
    "Magical_ManhwaRecaps", "MamoruManhwa", "TobsManhwa",
    "ManhwaVoidd", "Gave-k8y", "kawaiikotoYT", "manhwaexplorer5310",
    "John.Manhwa", "FuriosToon", "manhwadealer", "ManhwaRecapZone",
    "MrManhwas01", "Dazai_manhwa", "MobManhwa",
]
BACKFILL_DAYS = 305

HEADER = ["quero_postar", "obra", "canal", "data_postado", "viewers", "duracao", "link"]
DATE_FMT = "%d/%m/%Y %H:%M"
BRT = timezone(timedelta(hours=-3))


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


def parse_legacy_date_to_brt(s):
    if not s:
        return None
    try:
        return datetime.strptime(s, "%d/%m/%Y %H:%M").replace(tzinfo=BRT)
    except ValueError:
        pass
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc).astimezone(BRT)
    except ValueError:
        pass
    return None


def setup_formatting(spreadsheet, sheet):
    sheet_id = sheet.id
    requests = [
        {
            "updateSheetProperties": {
                "properties": {"sheetId": sheet_id, "gridProperties": {"frozenRowCount": 1}},
                "fields": "gridProperties.frozenRowCount",
            }
        },
        {
            "setDataValidation": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 1},
                "rule": {"condition": {"type": "BOOLEAN"}, "strict": False},
            }
        },
        {
            "repeatCell": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 3, "endColumnIndex": 4},
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "DATE_TIME", "pattern": 'dd/mm/yyyy" - "HH:mm'}}},
                "fields": "userEnteredFormat.numberFormat",
            }
        },
        {
            "repeatCell": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 4, "endColumnIndex": 5},
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
                "fields": "userEnteredFormat.numberFormat",
            }
        },
    ]
    spreadsheet.batch_update({"requests": requests})


def ensure_filter_covers_data(spreadsheet, sheet, data_row_count):
    md = spreadsheet.fetch_sheet_metadata()
    bf = None
    for s in md.get("sheets", []):
        if s.get("properties", {}).get("sheetId") == sheet.id:
            bf = s.get("basicFilter")
            break

    current_end = bf.get("range", {}).get("endRowIndex", 0) if bf else 0
    if current_end >= data_row_count:
        return

    new_filter = {
        "range": {
            "sheetId": sheet.id,
            "startRowIndex": 0,
            "endRowIndex": data_row_count,
            "startColumnIndex": 0,
            "endColumnIndex": 7,
        }
    }
    if bf:
        for key in ("sortSpecs", "criteria", "filterSpecs"):
            if bf.get(key):
                new_filter[key] = bf[key]
    requests = []
    if bf:
        requests.append({"clearBasicFilter": {"sheetId": sheet.id}})
    requests.append({"setBasicFilter": {"filter": new_filter}})
    spreadsheet.batch_update({"requests": requests})


def migrate_column_a_booleans(spreadsheet, sheet):
    last_row = sheet.row_count
    data = spreadsheet.values_get(
        f"'{sheet.title}'!A2:A{last_row}",
        params={"valueRenderOption": "UNFORMATTED_VALUE"},
    )
    values = data.get("values", [])
    updates = []
    for i, row in enumerate(values, start=2):
        if not row:
            continue
        v = row[0]
        if isinstance(v, str) and v.strip().upper() in ("FALSE", "TRUE"):
            updates.append({"range": f"A{i}", "values": [[v.strip().upper() == "TRUE"]]})
    if updates:
        sheet.batch_update(updates, value_input_option="USER_ENTERED")
    return len(updates)


def main():
    yt = build("youtube", "v3", developerKey=os.environ["YOUTUBE_API_KEY"])
    creds = Credentials.from_service_account_info(
        json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    spreadsheet = gspread.authorize(creds).open_by_key(SHEET_ID)
    sheet = spreadsheet.worksheet(SHEET_TAB)

    setup_formatting(spreadsheet, sheet)
    n_a_migrated = migrate_column_a_booleans(spreadsheet, sheet)

    rows = sheet.get_all_values()
    if not rows or rows[0] != HEADER:
        sheet.update([HEADER], "A1:G1")
        rows = sheet.get_all_values()

    existing_by_id = {}
    date_migrations = []
    for i, row in enumerate(rows[1:], start=2):
        if len(row) >= 7:
            vid = extract_video_id(row[6])
            if vid:
                existing_by_id[vid] = i
            if len(row) >= 4 and row[3] and "/" not in row[3]:
                dt = parse_legacy_date_to_brt(row[3])
                if dt:
                    date_migrations.append({"range": f"D{i}", "values": [[dt.strftime(DATE_FMT)]]})

    if date_migrations:
        sheet.batch_update(date_migrations, value_input_option="USER_ENTERED")

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
            try:
                r = yt.playlistItems().list(
                    part="contentDetails", playlistId=uploads,
                    maxResults=50, pageToken=page_token,
                ).execute()
            except HttpError as e:
                if e.resp.status == 404:
                    print(f"uploads playlist not accessible for @{handle} ({uploads}) — skipping")
                else:
                    print(f"error fetching @{handle}: {e}")
                break
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
            v["published"].astimezone(BRT).strftime(DATE_FMT),
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

    total_data_rows = 1 + len(existing_by_id) + len(new_rows)
    ensure_filter_covers_data(spreadsheet, sheet, total_data_rows)

    print(f"added {len(new_rows)} new, updated {len(updates)} viewer counts, migrated {len(date_migrations)} legacy dates, {n_a_migrated} checkboxes")


if __name__ == "__main__":
    main()
