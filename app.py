from flask import Flask, render_template, request, redirect, session
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = "secret123"

# ---------- LOGIN ----------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# ---------- GOOGLE SHEETS ----------
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
SHEET_ID = "17TWSyqu419rCFIEUB8H3p_b2bnHNa8pcI-ijxLNcj8M"
sheet = client.open_by_key(SHEET_ID).sheet1

# ---------- STATUS CHECK ----------
def check_deadlines():
    today = date.today()
    rows = sheet.get_all_values()

    for i in range(2, len(rows) + 1):
        row = sheet.row_values(i)
        while len(row) < 5:
            row.append("")
        deadline_str = row[3].strip()
        if deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                if deadline < today:
                    status = "Overdue"
                elif deadline == today:
                    status = "Due Today"
                else:
                    status = "Pending"
            except ValueError:
                status = "Invalid Date"
        else:
            status = "No Deadline"
        sheet.update_cell(i, 5, status)

# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == ADMIN_USERNAME and request.form["password"] == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect("/cases")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/add")
def add_page():
    if not session.get("logged_in"):
        return redirect("/")
    return render_template("index.html")

@app.route("/cases")
def view_cases():
    if not session.get("logged_in"):
        return redirect("/")
    check_deadlines()
    rows = sheet.get_all_values()[1:]
    return render_template("cases.html", cases=rows)

@app.route("/add_case", methods=["POST"])
def add_case():
    if not session.get("logged_in"):
        return redirect("/")
    sheet.append_row([
        request.form["case_id"],
        request.form["officer_name"],
        request.form["phone"],
        request.form["deadline"],
        "Pending"
    ])
    return redirect("/cases")

@app.route("/delete_case", methods=["POST"])
def delete_case():
    if not session.get("logged_in"):
        return redirect("/")
    sheet.delete_rows(int(request.form["sheet_row"]))
    return redirect("/cases")

if __name__ == "__main__":
    app.run(debug=True)
