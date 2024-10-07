import os

import requests


URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")

    res = requests.get(
        f"{URL}key={API_KEY}&q={CITY}"
    )
    data = res.json()

    location = data["location"]
    current_weather = data["current"]

    print(f"{location['name']}/{location['country']} "
          f"{location['localtime']} "
          f"Weather: {current_weather['temp_c']} Celsius, "
          f"{current_weather['condition']['text']}"
          )


if __name__ == "__main__":
    get_weather()
