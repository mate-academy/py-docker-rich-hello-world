import os
from datetime import datetime as dt

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("No API key found in environment variables")

    url = BASE_URL + f"key={api_key}&q={CITY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current_time = dt.now().strftime("%Y-%m-%d %H:%M")

        location = f"{data['location']['name']}/{data['location']['country']}"

        weather = (f"Weather: {data['current']['temp_c']} °C "
                   f"{data['current']['condition']['text']}")
        print(f"{location} {current_time} {weather}")
    else:
        print(f"Failed to get data. Status code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
