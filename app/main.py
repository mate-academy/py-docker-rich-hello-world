import os

import requests


API_KEY = os.environ.get("API_KEY")

API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q="

CITY = "Paris"


def get_weather() -> None:
    print(f"Getting weather for {CITY}")
    response = requests.get(f"{API_URL}?q={CITY}&key={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        print(f"Weather: {data}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
