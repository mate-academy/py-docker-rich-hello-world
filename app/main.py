import os

import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.weatherapi.com/v1/current.json"
FILTER = "Paris"


def get_weather() -> None:
    res = requests.get(
        BASE_URL, params={"key": os.getenv("API_KEY"), "q": FILTER}
    )
    print(res.content)


if __name__ == "__main__":
    get_weather()
