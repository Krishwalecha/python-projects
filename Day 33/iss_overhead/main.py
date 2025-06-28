import requests
import smtplib
from dotenv import load_dotenv
import os
from datetime import datetime
import time

load_dotenv()

# Load credentials
email = os.environ.get("EMAIL_USER")
password = os.environ.get("EMAIL_PASS")
recipient = os.environ.get("EMAIL_RECIPIENT")

LATITUDE = 18.508921
LONGITUDE = 73.926025

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude-LATITUDE) <= 5 and abs(iss_longitude-LONGITUDE) <= 5:
        return True
    
def is_nighttime():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0
    }

    response = requests.get(f'https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset_hour <= time_now <= sunrise_hour:
        return True

while True:
    time.sleep(60)
    if is_overhead() and is_nighttime():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=recipient, msg="Subject: Look Up! 👆\n\nThe ISS is above you in the sky.")
