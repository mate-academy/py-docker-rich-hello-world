import os
from datetime import datetime
from typing import Any

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError(
            "No API key found. "
            "Please set the API_KEY environment variable."
        )

    base_url = "https://api.weatherapi.com/v1"
    method = "current.json"
    location = "Paris"

    url = f"{base_url}/{method}?q={location}&key={api_key}"

    response = requests.get(url)

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
