import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    key = os.getenv("API_KEY")
    if not key:
        print("API_KEY environment variable not set")
        return
    params = {
        "q": "Paris",
        "key": key,
        "aqi": "no"
    }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {weather_data['location']['name']}:")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Weather: {weather_data['current']['condition']['text']}")
    else:
        print("Failed to get weather data")

if __name__ == "__main__":
    get_weather()
