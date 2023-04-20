import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": os.environ.get("API_KEY"),
        "q": FILTERING,
        "aqi": "no"
    }
    response = requests.get(URL, params=params)

    data = response.json()
    location = data["location"]
    current = data["current"]
    print(f"Performing request to Weather API for city {FILTERING}...")
    print(
        (
            f"{location['country']} "
            f"{location['name']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} "
            f"Celsius, {current['condition']['text']}"
        )
    )


if __name__ == "__main__":
    get_weather()
