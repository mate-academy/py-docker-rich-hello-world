import os

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
LOCATION = os.getenv("LOCATION")


def view_weather(response: Response) -> None:
    weather_data = response.json()
    print(f"Perform request to Weather API for city {LOCATION}...")
    print(
        f"{weather_data["location"]["country"]}/"
        f"{weather_data["location"]["name"]} "
        f"{weather_data["location"]["localtime"]} "
        f"Weather: {weather_data["current"]["temp_c"]}"
        f" Celsius {weather_data["current"]["condition"]["text"]}"
    )


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": LOCATION,
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        view_weather(response)
    else:
        print("Error to get weather:", response.status_code)


if __name__ == "__main__":
    get_weather()
