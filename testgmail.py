# testgmail.py
from gmail_api import authenticate_gmail, fetch_latest_emails

service = authenticate_gmail()
emails = fetch_latest_emails(service)
print(f"Found {len(emails)} emails.")
for email in emails:
    print("Subject:", email['subject'])
