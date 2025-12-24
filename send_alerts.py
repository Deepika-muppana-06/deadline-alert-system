from datetime import datetime
from twilio.rest import Client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

# ---------- LOAD .env ----------
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")

# ---------- GOOGLE SHEETS SETUP ----------
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)
client_gs = gspread.authorize(creds)

SHEET_ID = "17TWSyqu419rCFIEUB8H3p_b2bnHNa8pcI-ijxLNcj8M"
sheet = client_gs.open_by_key(SHEET_ID).sheet1

# ---------- TWILIO CLIENT ----------
client_twilio = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# ---------- SEND WHATSAPP ALERTS ----------
def send_alerts():
    rows = sheet.get_all_values()
    today = datetime.today().date()

    for row in rows[1:]:  # skip header
        try:
            case_id = row[0]
            officer_name = row[1]
            phone = row[2].strip()
            deadline_str = row[3].strip()

            if not phone.startswith("+"):
                phone = "+91" + phone

            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            except ValueError:
                print(f"❌ Invalid date for case {case_id}")
                continue

            days_left = (deadline - today).days

            if days_left > 3:
                continue
            elif days_left == 3:
                msg = f"Reminder: Case {case_id} is due in 3 days ({deadline_str}). Officer: {officer_name}"
            elif days_left == 1:
                msg = f"Reminder: Case {case_id} is due TOMORROW ({deadline_str}). Officer: {officer_name}"
            elif days_left == 0:
                msg = f"Reminder: Case {case_id} is due TODAY ({deadline_str}). Officer: {officer_name}"
            else:
                msg = f"ALERT: Case {case_id} is OVERDUE since {deadline_str}. Officer: {officer_name}"

            client_twilio.messages.create(
                body=msg,
                from_=TWILIO_WHATSAPP_FROM,
                to=f"whatsapp:{phone}"
            )

            print(f"✅ WhatsApp sent to {officer_name} ({phone})")

        except Exception as e:
            print(f"❌ Error processing case {case_id}: {e}")

if __name__ == "__main__":
    send_alerts()
