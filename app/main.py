import os

import requests


def get_weather() -> None:

    API_KEY = os.environ.get("API_KEY")
    CITY = "Paris"
    URL = "http://api.weatherapi.com/v1/current.json"

    res = requests.get(URL, {"key": API_KEY, "q": CITY}).json()

    print(f"City: {CITY}; Date: {res['location']['localtime']};"
          f" Current temperature: {res['current']['temp_c']} Celsius")


if __name__ == "__main__":
    get_weather()
