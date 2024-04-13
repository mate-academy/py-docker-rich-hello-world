import os

import requests


WEATHER_API_URL = "http://api.weatherapi.com/v1"

METHOD = "current.json"

CITY = "Paris"


def get_weather(api_key: str) -> None:
    url = f"{WEATHER_API_URL}/{METHOD}?key={api_key}&q={CITY}"

    try:
        data = requests.get(url).json()

        name = data["location"]["name"]
        weather_description = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]
        feels_like = data["current"]["feelslike_c"]
        wind_mph = data["current"]["wind_mph"]

        print(
            f"Weather in {CITY} ({name}): {weather_description}.\n"
        )
        print(
            f"Additional information: \n"
            f"\tTemperature is {temp_c} degrees Celsius "
            f"({temp_f} degrees Fahrenheit).\n"
            f"\tFeels like {feels_like} degrees Celsius.\n"
            f"\tWinter: {wind_mph} MPH."
        )

    except requests.exceptions.RequestException as exception:
        print(f"Get weather data error: '{exception}'")


if __name__ == "__main__":
    api_key = os.environ.get("API_KEY")
    if api_key:
        get_weather(api_key)
    else:
        print("Error: Weather API_KEY not found.")
