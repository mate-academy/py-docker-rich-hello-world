import os

import requests
from requests import HTTPError

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.weatherapi.com/v1"

CURRENT_WEATHER_REQUEST = "/current.json"

CITY = "Paris"

params = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather() -> None:
    current_weather_url = f"{BASE_URL}{CURRENT_WEATHER_REQUEST}"

    try:
        response = requests.get(url=current_weather_url, params=params)
        response.raise_for_status()
    except HTTPError:
        print("API KEY was not entered or entered incorrectly. Try again")

    else:
        result = response.json()

        location = result.get("location", {})
        city = location.get("name", {})

        print(f"Performing request to Weather API for city {city}...")

        country = location.get("country", {})
        localtime = location.get("localtime", {})

        current = result.get("current", {})
        temperature = current.get("temp_c", {})
        condition = current.get("condition", {}).get("text", {})

        print(
            f"{city}/{country} {localtime} "
            f"Weather: {temperature} Celsius, {condition}"
        )


if __name__ == "__main__":
    get_weather()
