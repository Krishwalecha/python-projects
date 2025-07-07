import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# ==== Configuration ====
load_dotenv()
API_KEY = os.environ.get("API_KEY")
OW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

LAT = 18.520430
LON = 73.856743
FORECAST_HOURS = 4  # Next 12 hours (4 data points of 3-hour intervals)

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.environ.get("TWILIO_FROM")
TWILIO_TO = os.environ.get("TWILIO_TO")

# ==== Functions ====

def get_weather_forecast():
    params = {
        "lat": LAT,
        "lon": LON,
        "appid": API_KEY,
        "cnt": FORECAST_HOURS,
        "units": "metric"
    }
    response = requests.get(OW_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()["list"]

def detect_rain_times(forecast_data):
    rain_times = []
    for data in forecast_data:
        weather_id = data["weather"][0]["id"]
        if weather_id < 600:  # Rain, drizzle, etc.
            time = data["dt_txt"].split(" ")[1]
            rain_times.append(time)
    return rain_times

def send_sms_alert(times):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    time_str = ', '.join(times)
    body = f" \n🌧️Rain expected at {time_str}. Don't forget your umbrella! ☂️"
    message = client.messages.create(
        body=body,
        from_=TWILIO_FROM,
        to=TWILIO_TO
    )
    print(f"SMS sent! Status: {message.status}")
    print(f"Message: {message.body}")

# ==== Main Logic ====
try:
    forecast = get_weather_forecast()
    rain_times = detect_rain_times(forecast)

    if rain_times:
        send_sms_alert(rain_times)
    else:
        print("✅ No rain for the next 12 hours. Enjoy your day!")
except requests.exceptions.RequestException as e:
    print("❌ Failed to retrieve weather data:", e)
except Exception as e:
    print("⚠️ An unexpected error occurred:", e)
