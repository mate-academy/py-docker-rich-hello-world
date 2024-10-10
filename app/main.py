import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    key = os.getenv("API_KEY")
    response = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={"q": "Paris", "key": key},
    )
    print(
        f"Actual temperature in Paris: {response.json()["current"]["temp_c"]}"
    )


if __name__ == "__main__":
    get_weather()
