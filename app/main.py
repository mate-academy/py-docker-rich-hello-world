import os

import requests

KEY = os.environ["API_KEY"]
CITY = "Ichnya"
API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather():
    request = requests.get(API_URL, params={"key": KEY, "q": CITY})
    response = request.json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    time = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    weather = response["current"]["condition"]["text"]

    print(
        f"Performing request to Weather Api for city {city}...\n"
        f"{city}/{country} {time} Weather: {temperature} Celsius, {weather}"
    )


if __name__ == "__main__":
    get_weather()
