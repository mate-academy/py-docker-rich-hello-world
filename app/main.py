import os

import requests

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"

if not API_KEY:
    raise ValueError("API_KEY must be set")


def get_weather() -> None:
    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING}).json()
    print(
        f"In {result['location']['country']} - {result['location']['name']}, "
        f"current weather temperature is {result['current']['temp_c']} celsius"
        f" and current condition is {result['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
