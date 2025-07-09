# Day 36 – Environment Setup

To run **Stock & News Alert System**, create a `.env` file [here](../Day%2036/) with the following content:

```env
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
GNEWS_API_KEY=your_gnews_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM=your_twilio_phone_number
TWILIO_TO=recipient_phone_number
```

> ⚠️ Do **not** commit the `.env` file. Ensure it's listed in `.gitignore`.