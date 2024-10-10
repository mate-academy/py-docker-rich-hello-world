import os

import requests


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"

def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")

    result = requests.get(f"{URL}?key={API_KEY}&q={FILTERING}")
    if result.status_code == 200:
        result = result.json()

        place = result["location"]["name"]
        country = result["location"]["country"]
        localtime = result["location"]["localtime"]
        temp_c = result["current"]["temp_c"]
        condition = result["current"]["condition"]["text"]

        print(
            f"{place}/{country} {localtime} "
            f"Weather: {temp_c} Celsius, {condition}"
        )

    else:
        print(f"Error with code {result.status_code} occurred")


if __name__ == "__main__":
    get_weather()
