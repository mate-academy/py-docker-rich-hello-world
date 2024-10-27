import os

import requests
from dotenv import load_dotenv

load_dotenv()  # Завантажуємо змінні з .env

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("API KEY not set")

    params = {
        "key": API_KEY,
        "q": FILTERING
    }
    response = requests.get(URL, params=params)

    print(response.json())


if __name__ == "__main__":
    get_weather()
