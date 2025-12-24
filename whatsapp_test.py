from twilio.rest import Client
from dotenv import load_dotenv
import os

# ---------- LOAD ENV VARIABLES ----------
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")

# ---------- TWILIO CLIENT ----------
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# ---------- SEND WHATSAPP MESSAGE ----------
def send_whatsapp_alert(phone_number, message):
    try:
        # Add India country code if missing
        if not phone_number.startswith("+"):
            phone_number = "+91" + phone_number

        client.messages.create(
            from_=TWILIO_WHATSAPP_FROM,
            body=message,
            to=f"whatsapp:{phone_number}"
        )

        print(f"✅ WhatsApp sent to {phone_number}")

    except Exception as e:
        print(f"❌ WhatsApp failed for {phone_number}: {e}")


# ---------- TEST ----------
if __name__ == "__main__":
    test_number = "8523870540"   # change to your joined sandbox number
    test_message = "✅ WhatsApp test successful from Deadline Alert System"
    send_whatsapp_alert(test_number, test_message)
