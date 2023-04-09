import os

import requests


API_KEY = os.getenv("API_KEY")
FILTERING = "Odesa"


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    params = {"key": API_KEY, "q": FILTERING}

    response = requests.get(url, params=params)

    print(response.content)


if __name__ == "__main__":
    get_weather()
