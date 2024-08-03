import os

import requests


KEY = os.environ["API_KEY"]
CITY = "Kyiv"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(f"{BASE_URL}?key={KEY}&q={CITY}",)
    data = response.json()
    print(f"Performing request to Weather API for city {CITY}...")
    print(f"{data['location']['name']}/{data['location']['country']}"
          f" {data['location']['localtime']} "
          f"Weather: {data['current']['temp_c']} "
          f"Celsius, {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
