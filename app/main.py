import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ["API_KEY"]
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(URL + f"?key={API_KEY}&q={FILTERING}")

    city = response.json().get("location").get("name")
    country = response.json().get("location").get("country")
    localtime = response.json().get("location").get("localtime")
    celsius = response.json().get("current").get("temp_c")
    condition = response.json().get("current").get("condition").get("text")

    print(f"Performing requests to Weather API for city {FILTERING}...")
    print(f"{city}/{country} {localtime} "
          f"Weather: {celsius} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
