import os
import requests
from dotenv import load_dotenv


load_dotenv()

CITY = "Paris"
API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    result_weather = requests.get(f"{URL}?key={API_KEY}&q={CITY}")
    if result_weather.status_code == 200:
        weather = result_weather.json()

        city = weather["location"]["name"]
        country = weather["location"]["country"]
        localtime = weather["location"]["localtime"]
        temp_c = weather["current"]["temp_c"]
        condition = weather["current"]["condition"]["text"]

        print(
            f"Performing request to weather API for city {city}...\n"
            f"{city}/{country} {localtime} Weather: {temp_c} Celsius, {condition}"
        )
    else:
        print(f"Error: {result_weather.status_code}")


if __name__ == "__main__":
    get_weather()
