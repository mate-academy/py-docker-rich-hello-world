import requests
import os
from dotenv import load_dotenv

load_dotenv()


FORMAT = "json"
BASE_URL = "http://api.weatherapi.com/v1"
CITY_NAME = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    url = f"{BASE_URL}/current.{FORMAT}?key={API_KEY}&q={CITY_NAME}"
    response = requests.get(url)
    print(response.status_code, response.json())


if __name__ == "__main__":
    get_weather()
