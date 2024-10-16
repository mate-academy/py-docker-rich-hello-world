import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    try:
        full_url = f"{BASE_URL}?key={API_KEY}&q={CITY}&aqi=no"

        response = requests.get(full_url)
        weather_data = response.json()

        location = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        temp_c = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        localtime = weather_data["location"]["localtime"]

        localtime = datetime.strptime(localtime, "%Y-%m-%d %H:%M")
        formatted_time = localtime.strftime("%Y-%m-%d %H:%M")

        print(f"Performing request to Weather API for city {location}...")
        print(
            f"{location}/{country} {formatted_time} "
            f"Weather: {temp_c}° Celsius, {condition}"
        )
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
