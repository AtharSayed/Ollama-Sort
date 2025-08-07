from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
TOKEN_FILE = 'token.json'

def authenticate_gmail():
    """
    Authenticates with the Gmail API.

    This function handles the OAuth 2.0 flow. It will look for a saved token.json
    file. If the file doesn't exist or is expired, it will open a web browser
    for a one-time authentication. After successful authentication, it saves
    the token to token.json for future use.

    Returns:
        googleapiclient.discovery.Resource: A service object for interacting with the Gmail API.
    """
    creds = None
    if os.path.exists(TOKEN_FILE):
        # Load credentials from the saved token file.
        from google.oauth2.credentials import Credentials
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        # If credentials don't exist or are invalid, initiate the OAuth flow.
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the updated credentials.
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service

def fetch_latest_emails(service, max_results=10):
    """
    Fetches a specified number of the most recent emails from the inbox.

    Args:
        service (googleapiclient.discovery.Resource): The authenticated Gmail service object.
        max_results (int): The maximum number of emails to fetch.

    Returns:
        list: A list of dictionaries, where each dictionary contains the email's ID,
              subject, and a snippet of the body.
    """
    emails = service.users().messages().list(userId='me', maxResults=max_results).execute().get('messages', [])
    email_list = []
    
    for email in emails:
        msg_data = service.users().messages().get(userId='me', id=email['id'], format='full').execute()
        headers = msg_data['payload']['headers']
        
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "")
        snippet = msg_data.get('snippet', "")
        
        email_list.append({'id': email['id'], 'subject': subject, 'snippet': snippet})

    return email_list
