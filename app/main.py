import os

import requests
from dotenv import load_dotenv

load_dotenv()
URL = "http://api.weatherapi.com/v1/current.json"
city = "Paris"


def get_weather() -> str:
    key = os.getenv("API_KEY")
    response = requests.get(
        URL,
        params={"q": city, "key": key},
    )
    return f"Temperature in Paris: {response.json()['current']['temp_c']}"


if __name__ == "__main__":
    get_weather()
