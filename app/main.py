import os
from dotenv import load_dotenv

import requests

load_dotenv()
URL = "https://api.weatherapi.com/v1/"
API_KEY = os.getenv("API_KEY")

FILTERING = "Paris"


def get_weather() -> None:
    print(API_KEY)
    response = requests.get(f"{URL}current.json?key={API_KEY}&q={FILTERING}")
    print(response.json())


if __name__ == "__main__":
    get_weather()
