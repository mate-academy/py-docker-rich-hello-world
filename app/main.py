import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    params = {
        "key": api_key,
        "q": os.getenv("CITY_NAME")
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return

    try:
        weather_data = response.json()
    except ValueError as e:
        print(e)
        return

    pprint(weather_data)


if __name__ == "__main__":
    get_weather()
