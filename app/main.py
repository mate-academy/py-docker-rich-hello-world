import os

import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"

API_KEY = os.environ.get("API_KEY")

city = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {city}...")
    response = requests.get(f"{BASE_URL}?q={city}&key={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        print(
            f'{data["location"]["tz_id"]} {data["current"]["last_updated"]} '
            f'Weather: {data["current"]["temp_c"]} Celsius, '
            f'{data["current"]["condition"]["text"]}'
        )
    else:
        print(f"An error occurred ({response.status_code})")


if __name__ == "__main__":
    get_weather()
