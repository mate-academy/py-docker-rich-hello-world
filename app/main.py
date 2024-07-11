import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather(api: str, location: str) -> None:
    print(f"Performing request to Weather API for city {location}")

    url = f"{URL}?key={api}&q={location}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]
        condition = current["condition"]
        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} "
            f"Celsius, {condition['text']}"
        )
    else:
        print(f"Failed {response.status_code}")


if __name__ == "__main__":
    if API_KEY:
        get_weather(API_KEY, "Paris")
    else:
        print("There is not API key. Stop work!")
