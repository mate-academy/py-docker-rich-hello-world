import os

import requests

API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    """
    Fetches current weather data for Paris city and displays it in the console.
    """
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {"key": api_key, "q": CITY}

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    data = response.json()

    location = data["location"]
    country = location["country"]
    current = data["current"]
    local_time = location["localtime"]
    current_temp = current["temp_c"]
    current_conditions = current["condition"]["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(
        f"{CITY}/{country} {local_time} Weather: {current_temp} Celsius, "
        f"{current_conditions}"
    )


if __name__ == "__main__":
    get_weather()
