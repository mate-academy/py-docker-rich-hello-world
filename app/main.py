import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    print("Performing request to Weather API for city paris...")
    request = requests.get(f"http://api.weatherapi.com/v1/current.json?"
                           f"key={os.getenv('API_KEY')}&q=Paris&aqi=no")

    temp = request.json()["current"]["temp_c"]
    weather = request.json()["current"]["condition"]["text"]
    time = request.json()["current"]["last_updated"]
    print(f"Paris/France {time} Weather: {temp} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
