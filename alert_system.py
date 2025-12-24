# List of current cases
cases = [
    {"id": 1, "name": "Case A", "alerted": False},
    {"id": 2, "name": "Case B", "alerted": False}
]

def send_alert(case):
    """Send alert for a single case"""
    print(f"Alert sent for {case['name']}")
    case["alerted"] = True

def add_new_case(case_name):
    """Add a new case and automatically alert"""
    new_id = max(case["id"] for case in cases) + 1 if cases else 1
    new_case = {"id": new_id, "name": case_name, "alerted": False}
    cases.append(new_case)
    print(f"New case added: {case_name}")
    
    # Automatically send alert for the new case
    send_alert(new_case)

# --- Demo ---
if __name__ == "__main__":
    # Send alerts for old cases
    for case in cases:
        if not case["alerted"]:
            send_alert(case)
    
    # Dynamically add new cases
    add_new_case("Case C")
    add_new_case("Case D")
