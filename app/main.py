import os
import requests
from typing import Optional

API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather(api_key: str, city: str) -> str:
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"Weather report for {location}: {temp_c}°C, {condition}"
    else:
        return "Failed to get weather data"


if __name__ == "__main__":
    if not API_KEY:
        raise ValueError("API_KEY environment variable is not set")
    print(get_weather(API_KEY, CITY))
