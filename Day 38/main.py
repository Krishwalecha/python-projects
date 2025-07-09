import requests
from os import environ
from dotenv import load_dotenv
from datetime import datetime

# ---------- Load Environment Variables ----------
load_dotenv()

APP_ID = environ.get("APP_ID")
API_KEY = environ.get("API_KEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/d9700a14c9bf8bafa1de2a9d90eb456d/myWorkouts/sheet1"

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 177
AGE = 20

# ---------- Functions ----------
def get_exercises(description : str) -> list[dict]:
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "0"
    }

    exercise_params = {
        "query": description,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    response = requests.post(EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result["exercises"]

def log_exercise_to_sheet(exercise):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")

    sheety_data = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": str(exercise["duration_min"]) + " mins",
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(SHEETY_ENDPOINT, json=sheety_data)
    response.raise_for_status()
    print(response.text)

# ---------- Main ----------
def main():
    user_input = input("Describe the exercise you did today: ")
    exercises = get_exercises(user_input)
    for exercise in exercises:
        log_exercise_to_sheet(exercise)

if __name__ == "__main__":
    main()
