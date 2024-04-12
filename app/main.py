import os

import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
REGION = "paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    params = {"key": API_KEY, "q": REGION, "aqi": "no"}
    response = requests.get(URL, params=params)
    response.raise_for_status()

    result = response.json()

    for key, value in result.get("location", {}).items():
        print(f"{key}: {value}")

    for key in ("temp_c", "wind_kph", "wind_dir", "humidity", "last_updated"):
        print(f"{key}: ", result.get("current", {}).get(key))


if __name__ == "__main__":
    get_weather()
