import requests
import json
from os import environ
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

PIXELA_TOKEN = environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"

BASE_URL = "https://pixe.la/v1/users"
GRAPH_URL = f"{BASE_URL}/{PIXELA_USERNAME}/graphs"
PIXEL_URL = f"{GRAPH_URL}/{GRAPH_ID}"

HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

def create_user():
    payload = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(BASE_URL, json=payload)
    print("[User] Create:", response.text)

def create_graph():
    payload = {
        "id": GRAPH_ID,
        "name": "Python Graph",
        "unit": "Hours",
        "type": "float",
        "color": "sora"
    }
    response = requests.post(GRAPH_URL, json=payload, headers=HEADERS)
    print("[Graph] Create:", response.text)

def add_pixel(date=None, quantity="1.0", note=None):
    if not date:
        date = datetime.today().strftime("%Y%m%d")

    payload = {
        "date": date,
        "quantity": quantity,
    }

    if note:
        payload["optionalData"] = json.dumps({"note": note})

    response = requests.post(PIXEL_URL, json=payload, headers=HEADERS)
    print(f"[Pixel] Add ({date}):", response.text)

def update_pixel(date, new_quantity="1.0"):
    payload = {
        "quantity": new_quantity
    }
    response = requests.put(f"{PIXEL_URL}/{date}", json=payload, headers=HEADERS)
    print(f"[Pixel] Update ({date}):", response.text)


def delete_pixel(date):
    response = requests.delete(f"{PIXEL_URL}/{date}", headers=HEADERS)
    print(f"[Pixel] Delete ({date}):", response.text)

# === EXAMPLE USAGE ===

# create_user()
# create_graph()

# add_pixel(quantity="2.5", note="Learned Pixela API and practiced Python automation.")
# update_pixel(date="20250709", new_quantity="3.0")

# delete_pixel(date="20250708")
