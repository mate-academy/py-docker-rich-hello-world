import os

import requests
from dotenv import load_dotenv

load_dotenv()  # Завантажуємо змінні з .env

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Kyiv"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING
    }
    response = requests.get(URL, params=params)

    print(response.json())


if __name__ == "__main__":
    get_weather()
