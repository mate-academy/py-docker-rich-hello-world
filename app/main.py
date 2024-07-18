import os

import requests
from dotenv import load_dotenv

from weather_types import WeatherData

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather(city: str) -> WeatherData | None:
    params = {
        "key": API_KEY,
        "q": city,
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None

    return response.json()


def main() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")
    weather_data = get_weather(FILTERING)

    if not weather_data:
        print("Something went wrong.")
    else:
        city = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        datetime = weather_data["location"]["localtime"]
        condition = weather_data["current"]["condition"]["text"]
        temp_celsius = weather_data["current"]["feelslike_c"]
        print(f"{city}/{country} {datetime} "
              f"Weather: {temp_celsius} Celsius, {condition}")


if __name__ == "__main__":
    main()
