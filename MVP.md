# MVP Document

## Project Title
Automated Case Deadline Alert and Tracking System

---

## Problem Statement
Time-bound cases often face delays because officers do not receive timely reminders about approaching deadlines. The lack of automated SMS or WhatsApp alerts leads to missed actions, slower investigations, and reduced efficiency in case management.

---

## Proposed Solution
A lightweight, web-based system that tracks case deadlines and automatically sends SMS or WhatsApp alerts to responsible officers before and after deadlines. The system uses a simple data store and automated checks to ensure timely notifications without manual follow-ups.

---

## MVP Features
(Minimum features required for a working solution)

- Case details stored in Google Sheets  
- Fields: Case ID, Officer Name, Phone Number, Deadline, Status  
- Automatic daily deadline check  
- SMS or WhatsApp alert sent before deadline  
- Case status updated as Pending or Overdue  

---

## Technology Stack
- Frontend: HTML, CSS  
- Backend: Python (Flask)  
- Database: Google Sheets  
- Alerts: Twilio API (SMS / WhatsApp)  
- Hosting: GitHub Pages (Frontend)  

---

## Future Scope
- AI-based priority prediction for urgent cases  
- Multilingual SMS and WhatsApp alerts  
- Officer-wise dashboard and analytics  
- Role-based access for admin and officers  
- Mobile application support
