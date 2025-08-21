# Google Calendar to Printer

This project allows you to automatically print events from your Google Calendar using a USB printer. It utilizes the Google Calendar API to fetch events and the `escpos` library to handle printing.

## Features

- Fetches events from Google Calendar.
- Prints event details including name, due date, and description.
- Webhook integration to listen for calendar updates.

## Requirements

- Python 3.x
- `google-auth-oauthlib`
- `google-api-python-client`
- `fastapi`
- `uvicorn`
- `python-escpos`

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd googleCalendarToPrinter
   ```

2. **Install dependencies:**
   ```bash
   pip install google-auth-oauthlib google-api-python-client fastapi uvicorn python-escpos
   ```

3. **Obtain Google Calendar API credentials:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project and enable the Google Calendar API.
   - Create credentials (OAuth 2.0 Client IDs) and download the `client_secret.json` file.
   - Place the `client_secret.json` file in the project directory.

4. **Run the authentication script to generate token:**
   ```bash
   python getApiKey.py
   ```

5. **Start the FastAPI server:**
   ```bash
   python api.py
   ```

6. **Set up the calendar watch:**
   - Run the following script to start watching for calendar updates:
   ```bash
   python watchCalendar.py
   ```

## Usage

- The application will listen for updates to your Google Calendar and print new or updated events to the connected USB printer.
- Ensure your printer is connected and configured correctly with the appropriate Vendor ID and Product ID in `recieptPrinter.py`.

## Notes

- Modify the `VENDOR_ID` and `PRODUCT_ID` in `recieptPrinter.py` to match your printer's specifications.
- The webhook address in `watchCalendar.py` should point to your FastAPI endpoint.

## License

This project is licensed under the MIT License.