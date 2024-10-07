import json
import os

import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"
CITY = "Paris"


def get_weather(city: str) -> None:
    endpoint = "/current.json"
    response = requests.get(
        BASE_URL + endpoint,
        params={
            "key": API_KEY,
            "q": city,
        }
    )

    data = json.loads(response.text)
    data_city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        "Performing request to Weather API for city Paris...\n"
        f"{data_city}/{country} {localtime} "
        f"Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather(CITY)
