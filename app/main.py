import io
import json
import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ["API_KEY"]
FILTERING = "Paris"


def get_weather() -> None:
    print("Performing request to WEATHER API for Paris city...")
    open_url = requests.get(f"{URL}?key={API_KEY}&q={FILTERING}")

    response = json.load(io.BytesIO(open_url.content))
    location = response["location"]
    weather = response["current"]
    print(
        f"{location['name']}/{location['country']} {location['localtime']}, "
        f"Weather: {weather['temp_c']} Celsius, {weather['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
