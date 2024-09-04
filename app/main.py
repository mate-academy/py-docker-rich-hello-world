import os
from datetime import datetime

import requests


API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        print("No API key provided")
        return

    params = {
        "q": "Paris",
        "key": API_KEY,
        "aqi": "no"
    }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city = "Paris/France"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        temp_celsius = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"{city} {current_time} "
              f"Weather: {temp_celsius} "
              f"Celsius, {condition}")
    else:
        print("Failed to retrieve weather data")


if __name__ == "__main__":
    get_weather()
