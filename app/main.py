import os
import requests


def get_weather() -> None:
    API_KEY = os.environ.get("API_KEY")
    CITY = "Paris"
    URL = "http://api.weatherapi.com/v1/current.json?"

    res = requests.get(URL + f"key={API_KEY}&q={CITY}")

    data = res.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    date = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    sky = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")
    print(f"{city}/{country} {date} Weather: {temperature}, {sky}")


if __name__ == "__main__":
    get_weather()
