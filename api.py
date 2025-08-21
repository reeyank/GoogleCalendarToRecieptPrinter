from fastapi import FastAPI, Request
import pickle
from googleapiclient.discovery import build
import datetime
import uvicorn
from recieptPrinter import calendar_to_reciept

# Load credentials from token.pkl
with open('token.pkl', 'rb') as f:
    creds = pickle.load(f)

service = build("calendar", "v3", credentials=creds)
app = FastAPI()

# Store last time we fetched events (UTC)
last_checked = datetime.datetime.utcnow()

@app.post("/calendar-webhook")
async def calendar_webhook(request: Request):
    global last_checked
    headers = request.headers
    resource_state = headers.get("X-Goog-Resource-State")

    if resource_state == "exists":
        updated_min = last_checked.isoformat() + "Z"
        events_result = service.events().list(
            calendarId="primary",       # replace with your specific calendar ID
            orderBy="updated",
            updatedMin=updated_min,
            singleEvents=True,
            showDeleted=False,          # do NOT include deleted events
            maxResults=50
        ).execute()

        events = events_result.get("items", [])

        if events:
            print(f"🆕 {len(events)} new/updated events (excluding deleted):")
            for event in events:
                if "description" in event and event["description"]:
                    calendar_to_reciept(name=event["summary"], description=event["description"], due=event["start"]["date"])
                else:
                    calendar_to_reciept(name=event["summary"], description="N/A", due=event["start"]["date"])

        # Update last_checked to now
        last_checked = datetime.datetime.utcnow()

    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
