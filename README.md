# Deadline Alert System

A simple system to track deadlines and send WhatsApp alerts to officers using Google Sheets and Twilio.

## Features

- Sends WhatsApp notifications for:
  - Cases due in 3 days
  - Cases due tomorrow
  - Cases due today
  - Overdue cases
- Tracks case deadlines from a Google Sheet
- Admin login to add or delete cases
- Uses `.env` file to securely store Twilio credentials

## Technologies Used

- Python 3
- Twilio API (WhatsApp)
- Google Sheets API (`gspread` and `oauth2client`)
- Flask (for the web app)
- dotenv (for environment variables)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Deepika-muppana-06/deadline-alert-system.git
cd deadline_alert_system
