import os
from datetime import datetime

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError(
            "No API key found. "
            "Please set the API_KEY environment variable."
        )

    url = "https://api.weatherapi.com/v1/current.json"
    location = "Paris"

    params = {
        "key": api_key,
        "q": location,
    }

    response = requests.get(url, params=params)

    print(f"Performing request to Weather API for city {location}")
    if response.status_code == 200:
        weather_data = response.json()
        city = "Paris/France"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        temp_celsius = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        print(f"{city} {current_time} "
              f"Weather {temp_celsius} "
              f"Celsius, {condition}")
    else:
        print(f"{response.status_code} {response.text}")


if __name__ == "__main__":
    get_weather()
