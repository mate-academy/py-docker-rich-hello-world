import os
from typing import Any

import requests


def get_weather() -> dict[str, str] | Any:
    api_key = os.getenv("API_KEY")
    url = "https://api.weatherapi.com/v1/current.json?"
    city = "Paris"

    res = requests.get(url + f"key={api_key}&q={city}")

    if res.status_code == 200:
        data = res.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        date = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        sky = data["current"]["condition"]["text"]

        print(f"Performing request to Weather API for city {city}...")
        print(f"{city}/{country} {date} Weather: {temperature}, {sky}")
        return data
    else:
        return {"error": f"{city} not found"}


if __name__ == "__main__":
    get_weather()
