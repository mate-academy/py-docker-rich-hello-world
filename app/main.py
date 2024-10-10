import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
CITY_NAME = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    params = {
        "key": api_key,
        "q": CITY_NAME
    }

    response = requests.get(URL, params=params)
    weather_data = response.json()
    pprint(weather_data)


if __name__ == "__main__":
    get_weather()
