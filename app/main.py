import os

import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
params = {"key": API_KEY, "q": "Paris"}


def get_weather() -> None:
    res = requests.get(BASE_URL, params=params)
    data = json.loads(res.text)
    location_name = data["location"]["name"]
    location_country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition_text = data["current"]["condition"]["text"]

    print(f"{location_name}/{location_country}")
    print(f"{localtime}")
    print(f"Weather: {temp_c} Celsius, {condition_text}")


if __name__ == "__main__":
    get_weather()
