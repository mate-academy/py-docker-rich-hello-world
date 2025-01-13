import os

import requests


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY", "No API key provided")
    CITY = os.getenv("CITY", "Kyiv")
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        weather_data = (
            weather_data["location"]["country"],
            weather_data["location"]["name"],
            weather_data["location"]["localtime"],
            f"Weather: {weather_data['current']['temp_c']} Celsius",
            weather_data["current"]["condition"]["text"])
        print(weather_data)
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
