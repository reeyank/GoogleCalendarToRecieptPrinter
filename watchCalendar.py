from googleapiclient.discovery import build
import pickle

# Load credentials
with open('token.pkl', 'rb') as f:
    creds = pickle.load(f)

service = build('calendar', 'v3', credentials=creds)

watch_request = {
    "id": "my-calendar-webhook-001",
    "type": "web_hook",
    "address": "https://calendar.reeyan.win/calendar-webhook"  # your FastAPI endpoint
}

response = service.events().watch(calendarId='primary', body=watch_request).execute()
print(response)
