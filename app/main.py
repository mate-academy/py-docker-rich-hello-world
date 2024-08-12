import os
from dotenv import load_dotenv

import requests

load_dotenv()

KEY_API = os.environ.get("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "q=Paris"


def get_weather() -> None:
    try:
        result = requests.get(URL + "?" + FILTERING, params={"key": KEY_API})
        data = result.json()
        location = f'{data["location"]["name"]} {data["location"]["country"]}'
        weather = (f'{data["current"]["temp_c"]}, '
                   f'{data["current"]["condition"]["text"]}')
        localtime = data["location"]["localtime"]
        print(f"Weather in: {location}, \n"
              f"Time: {localtime}. Temperature now: {weather}")
    except requests.exceptions.ConnectionError:
        print("Something went wrong, please try again later.")


if __name__ == "__main__":
    get_weather()
