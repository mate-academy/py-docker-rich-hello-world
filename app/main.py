import os

import requests

API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
UNIT = "Celsius"


def get_weather() -> None:
    json = requests.get(f"{URL}?key={API_KEY}&q={CITY}&aqi=no").json()

    if json:
        time = json.get("location").get("localtime")
        country = json.get("location").get("country")
        temp = json.get("current").get("temp_c")
        condition = json.get("current").get("condition").get("text")

        print(f"Performing request to Weather API for city {CITY}...\n"
              f"{CITY}/{country} {time} Weather: {temp} {UNIT}, {condition}")


if __name__ == "__main__":
    get_weather()
