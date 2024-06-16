import os
import requests

from dotenv import load_dotenv

load_dotenv()


CITY = "Paris"
API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}

    data = requests.get(URL, params).json()

    country = data["location"]["country"]
    last_updated = data["current"]["last_updated"]
    temp_celsius = data["current"]["temp_c"]
    weather_text = data["current"]["condition"]["text"]

    print(
        f"Weather API request for {CITY}/{country}\n"
        f"Date/Time: {last_updated}\n"
        f"Weather: {temp_celsius} Celsius, {weather_text}"
    )


if __name__ == "__main__":
    get_weather()
