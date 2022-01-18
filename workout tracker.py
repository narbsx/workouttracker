import requests
from datetime import datetime
import os

GENDER = YOUR GENDER 
WEIGHT = YOUR WEIGHT IN KG
HEIGHT = YOUR HEIGHT IN CM
AGE = YOUR AGE

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
TRACKER_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
POST_ENDPOINT = os.environ.get("POST_ENDPOINT")
excerise_text =input("Tell me what excerise you did:")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": excerise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(TRACKER_ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(result)

today = datetime.now()
today_date = today.strftime("%d/%m/%y")
now_time = today.strftime("%X")

for exercise in result["exercises"]:
    tracker_post = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
header_sheety = {
    'Content-Type': 'application/json',
    "Authorization": os.environ.get("TOKEN")
}

response = requests.post(url=POST_ENDPOINT, json=tracker_post, headers=header_sheety)
print(response.text)
