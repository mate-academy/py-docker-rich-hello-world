import requests

import os

from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    params = {
        "key": os.getenv("WEATHER_API_KEY"),
    }

    get_weather_in_paris_url = ("http://api.weatherapi.com/v1/"
                                "current.json?q=Paris")

    response = requests.get(get_weather_in_paris_url, params=params)
    weather = response.json()

    if weather:
        location = weather.get("location")
        current = weather.get("current", {})
        print(f"Country: {location["country"]}")
        print(f"City: {location["name"]}")
        print(f"Region: {location["region"]}")
        print(f"{location["localtime"]}")
        print(f"Temperature: {current["temp_c"]} celsius")

    else:
        print("Weather is currently unavailable")


if __name__ == "__main__":
    get_weather()
