import os

import requests

from dotenv import load_dotenv

load_dotenv()

WEATHER_URL = "http://api.weatherapi.com/v1/current.json"
KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not KEY:
        print("Please, provide weather API key")
        return
    params = {
        "q": "Paris",
        "key": KEY,
        "aqi": "no"
    }
    response = requests.get(WEATHER_URL, params)
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {weather_data['location']['name']}:\n"
              f"Temperature: {weather_data['current']['temp_c']}°C \n"
              f"Weather: {weather_data['current']['condition']['text']}s")
    else:
        print("Failed to get weather data")


if __name__ == "__main__":
    get_weather()
