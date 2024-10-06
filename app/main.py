import os
from datetime import datetime

import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
city = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("API_KEY is not set. Please set it as an environment variable.")
        return

    print(f"Performing request to Weather API for city {city}...")

    try:
        response = requests.get(f"{BASE_URL}?q={city}&key={API_KEY}")
        response.raise_for_status()
        weather_data = response.json()

        if "location" in weather_data and "current" in weather_data:
            location = weather_data["location"]
            current_weather = weather_data["current"]
            country = location["country"]
            temperature = current_weather["temp_c"]
            condition = current_weather["condition"]["text"]

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

            print(
                f"{city}/{country} {current_time} "
                f"Weather: {temperature: .1f} Celsius, {condition}"
            )

        else:
            print("No current weather data found.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
