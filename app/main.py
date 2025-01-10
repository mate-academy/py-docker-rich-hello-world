import os
from pprint import pprint

from dotenv import load_dotenv

import requests

load_dotenv()
URL = "https://api.weatherapi.com/v1/"
API_KEY = os.getenv("API_KEY")

FILTERING = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")
    response = requests.get(f"{URL}current.json?key={API_KEY}&q={FILTERING}")
    data = response.json()

    location = data.get("location", {})
    current = data.get("current", {})

    city = location.get("name", "")
    country = location.get("country", "")
    date = location.get("localtime", "")
    temperature = current.get("temp_c", "")
    condition = current.get("condition", {}).get("text", "")

    print(
        f"{city}/{country} {date} Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
