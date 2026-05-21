"""Lightweight job: refresh only the viewers column for all videos in the sheet."""
import os
import json
import re
from googleapiclient.discovery import build
import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = "1ordgWcnAmJpxAVD8qXy0dXjhgqu5Y_g2LkJFnzxA9f0"
SHEET_TAB = "todos"


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
    by_id = {}
    for i, row in enumerate(rows[1:], start=2):
        if len(row) >= 7:
            vid = extract_video_id(row[6])
            if vid:
                by_id[vid] = i

    stats = {}
    for batch in chunk(list(by_id.keys()), 50):
        r = yt.videos().list(part="statistics", id=",".join(batch)).execute()
        for it in r["items"]:
            stats[it["id"]] = int(it["statistics"].get("viewCount", 0))

    updates = []
    for vid, row_num in by_id.items():
        if vid in stats:
            updates.append({"range": f"E{row_num}", "values": [[stats[vid]]]})
    if updates:
        sheet.batch_update(updates)

    print(f"refreshed {len(updates)} viewer counts")


if __name__ == "__main__":
    main()
