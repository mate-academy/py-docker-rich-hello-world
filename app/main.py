import os
from datetime import datetime as dt

from dotenv import load_dotenv
import requests

load_dotenv()
BASE_URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("No API key found in environment variables")

    url = BASE_URL + f"key={api_key}&q={CITY}"
    response = requests.get(url).json()
    current_time = dt.now().strftime("%Y-%m-%d %H:%M")

    location = (f'{response["location"]["name"]}'
                f'/{response["location"]["country"]}')
    weather = (f'Weather: {response["current"]["temp_c"]} Celsius '
               f'{response["current"]["condition"]["text"]}')

    print(f"{location} {current_time} {weather}")


if __name__ == "__main__":
    get_weather()
