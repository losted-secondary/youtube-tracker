"""Aplica somente os nomes já revisados; não coleta vídeos nem envia mensagens."""
import argparse
import json
import os

import gspread
from google.oauth2.service_account import Credentials
from reviewed_identifications import apply_reviewed

SHEET_ID = "1ordgWcnAmJpxAVD8qXy0dXjhgqu5Y_g2LkJFnzxA9f0"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not os.environ.get("GOOGLE_CREDENTIALS_JSON"):
        parser.error("Defina GOOGLE_CREDENTIALS_JSON usando a conta de serviço do tracker.")
    creds = Credentials.from_service_account_info(
        json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    spreadsheet = gspread.authorize(creds).open_by_key(SHEET_ID)
    apply_reviewed(spreadsheet, spreadsheet.worksheet("todos"), dry_run=args.dry_run)
