import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        weather_paris = response.json()
        time_paris = weather_paris["current"]["last_updated"]
        temp_paris = weather_paris["current"]["temp_c"]
        sky_type = weather_paris["current"]["condition"]["text"]
        print(f"Paris/France {time_paris} "
              f"Weather: {temp_paris} Celsius, {sky_type}")
    else:
        print(f"Something wrong. Status code: {response.status_code}, "
              f"message: {response.text}")


if __name__ == "__main__":
    get_weather()
