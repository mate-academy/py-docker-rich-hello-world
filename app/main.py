import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.environ["API_KEY"]
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        f"{BASE_URL}?key={KEY}&q={CITY}",
    )
    return print(response.json())


if __name__ == "__main__":
    get_weather()
