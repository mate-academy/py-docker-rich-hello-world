import os
import requests


API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    print(f"Start request to Weather API for city {FILTERING}...")
    res = requests.get(URL, params={"key": API_KEY, "q": FILTERING})

    data = res.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temp_celsius = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]

    print(
        f"{city}/{country} "
        f"{local_time} Weather: {temp_celsius} Celsius, {weather}"
    )


if __name__ == "__main__":
    get_weather()
