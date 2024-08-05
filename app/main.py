import os
import requests
from dotenv import load_dotenv


def get_weather(key: str, city: str = "Paris") -> None:
    url = "https://api.weatherapi.com/v1/current.json"
    response = requests.get(
        url, params={
            "key": key,
            "q": city
        }
    )
    if response.status_code == 200:
        weather_data = response.json()
        location_localtime = weather_data["location"]["localtime"]
        location_name = weather_data["location"]["name"]
        location_country = weather_data["location"]["country"]
        location_weather = weather_data["current"]["condition"]["text"]
        location_wind = weather_data["current"]["wind_mph"]
        temp_c = weather_data["current"]["temp_c"]

        print(
            f"[{location_localtime}] {location_name} / {location_country}\n"
            f"Weather: {temp_c} C, {location_weather}, {location_wind} mph\n"
        )
    else:
        print(f"Failed to get weather data: {response.status_code}")


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if api_key:
        get_weather(key=api_key, city="Paris")
    else:
        raise ValueError("API key was not found.")
