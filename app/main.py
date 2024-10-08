import os
from datetime import datetime

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.environ.get("API_KEY")
API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q="
CITY = "Paris"


def get_weather() -> None:
    full_url = f"{API_URL}{CITY}&aqi=no"
    weather_data = {}

    try:
        response = requests.get(full_url)
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

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

if __name__ == "__main__":
    get_weather()
