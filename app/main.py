import os
import requests
from requests.exceptions import ConnectionError

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1"
CURRENT_WEATHER_REQUEST = "/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }
    current_weather_url = f"{BASE_URL}{CURRENT_WEATHER_REQUEST}"

    try:
        response = requests.get(current_weather_url, params=params)
        response.raise_for_status()

        result = response.json()
        location = result.get("location", {})
        current = result.get("current", {})

        city = location.get("name", "")
        country = location.get("country", "")
        localtime = location.get("localtime", "")
        temperature = current.get("temp_c", "")
        condition = current.get("condition", {}).get("text", "")

        print(f"Performing request to Weather API for city {city}...")
        print(f"{city}/{country} {localtime} Weather: {temperature} Celsius, {condition}")

    except ConnectionError:
        print("Failed to connect to the Weather API.")
    except requests.HTTPError:
        print("Invalid API KEY or request failed.")


if __name__ == "__main__":
    get_weather()
