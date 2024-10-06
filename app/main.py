import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    result = requests.get(f"{URL}?key={KEY}&q={FILTERING}").json()
    location = result["location"]
    current = result["current"]
    print(f"{location['name']}/{location['country']} "
          f"{location['localtime']} Weather: {current['temp_c']} Celsius,"
          f" {current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
