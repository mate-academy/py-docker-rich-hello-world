import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris"
    }

    response = requests.get(url, params=params)
    weather_data = response.json()
    pprint(weather_data)


if __name__ == "__main__":
    get_weather()
