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
        print(
            f"Performing request to Weather API "
            f"for city {location.get("name", {})}..."
        )

        current = result.get("current", {})
        condition = current.get("condition", {})
        print(
            f"{location.get("name", {})}/{location.get("country", {})} "
            f"{location.get("localtime", {})} Weather: "
            f"{current.get("temp_c", {})} Celsius, {condition.get("text", {})}"
        )


if __name__ == "__main__":
    get_weather()
