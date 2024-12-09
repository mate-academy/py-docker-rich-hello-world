import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable is required")


def get_weather():
    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no"
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        weather_data = response.json()

        temp_celsius = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        print(f"Weather in {CITY}: {temp_celsius}°C, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
