import os
from dotenv import load_dotenv
import requests

load_dotenv()

# flake8: noqa: N806
def get_weather() -> None:
    URL = "https://api.weatherapi.com/v1/current.json"
    KEY = os.getenv("WEATHER_API_KEY")
    FILTERING = "Paris"

    response = requests.get(f"{URL}?key={KEY}&q={FILTERING}")
    response = response.json()
    print(f"Performing request to Weather API for city {FILTERING}...")

    city = response["location"]["name"]
    country = response["location"]["country"]
    localtime = response["location"]["localtime"]
    weather_celsius = response["current"]["temp_c"]
    weather_condition = response["current"]["condition"]["text"]

    date, time = localtime.split(" ")

    result = (f"{city}/{country} {date} {time} "
              f"Weather: {weather_celsius} Celsius, {weather_condition}")
    print(result)


if __name__ == "__main__":
    get_weather()
