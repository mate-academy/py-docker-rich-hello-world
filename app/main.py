import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    try:
        print(f"Performing request to Weather API for city {FILTERING}...")
        response = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
        response.raise_for_status()
        data = response.json()

        print(
            f"{data['location']['name']}/"
            f"{data['location']['country']} "
            f"{data['location']['localtime']} "
            f"Weather: {data['current']['temp_c']} Celsius, "
            f"{data['current']['condition']['text']}"
        )
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
