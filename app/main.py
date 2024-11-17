import os

import requests


API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY is not specified")

    weather = requests.get(URL + f"?key={API_KEY}" + f"&q={FILTERING}").json()

    print(
        f"Performing request to Weather API for city "
        f"{weather.get('location').get('name')}..."
    )
    print(
        f"{weather.get('location').get('name')}/"
        f"{weather.get('location').get('country')} "
        f"{weather.get('location').get('localtime')} "
        f"Weather: {weather.get('current').get('temp_c')} Celsius, "
        f"{weather.get('current').get('condition').get('text')}"
    )


if __name__ == "__main__":
    get_weather()
