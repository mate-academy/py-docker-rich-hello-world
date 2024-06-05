import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = "e76c81a005944e4bac6142817240406"
KEY = os.getenv("API_KEY")
CITY = "Paris"

URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather() -> None:
    weather = requests.get(URL, params={"key": KEY, "q": CITY}).json()
    print(
        f"{weather["location"]["name"]}({weather["location"]["country"]})\n"
        f"Time: {weather["location"]["localtime"]}\n"
        f"Weather: {weather["current"]["temp_c"]} Celsius"
    )


if __name__ == "__main__":
    get_weather()
