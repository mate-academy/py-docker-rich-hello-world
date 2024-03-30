import os

import requests


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
payload = {"key": API_KEY, "q": CITY}
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    try:
        response = requests.get(URL, params=payload)
        data = response.json()
        county_name = data["location"]["country"]
        local_time = data["location"]["localtime"]
        celsius = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(
            f"In {CITY}/{county_name} {local_time} "
            f"Weather {celsius} Celsius, {condition}"
        )
    except requests.exceptions.ConnectionError:
        print("Connection")


if __name__ == "__main__":
    get_weather()

