import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"
KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not KEY:
        print("API_KEY environment variable not set")
        return
    params = {
        "q": "Paris",
        "key": KEY,
        "aqi": "no"
    }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {weather_data['location']['name']}: "
              f"Temperature: {weather_data['current']['temp_c']}°C,"
              f" Weather: {weather_data['current']['condition']['text']}")
    else:
        print("Failed to get weather data")


if __name__ == "__main__":
    get_weather()
