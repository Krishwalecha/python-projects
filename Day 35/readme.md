# Day 35 – Environment Setup

To run **Rain Alert System**, create a `.env` file [here](../Day%2035/) with the following content:

```env
API_KEY=your_openweather_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM=your_twilio_phone_number
TWILIO_TO=recipient_phone_number
```

> ⚠️ Do **not** commit the `.env` file. Ensure it's listed in `.gitignore`.