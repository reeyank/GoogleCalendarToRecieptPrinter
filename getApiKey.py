from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES
)
creds = flow.run_local_server(port=8000)  # This opens a browser to authorize

# Save creds for reuse
import pickle
with open('token.pkl', 'wb') as f:
    pickle.dump(creds, f)
