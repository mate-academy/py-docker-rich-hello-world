import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1"
ENDPOINT = "/current.json"


def get_weather() -> None:
    complete_url = f"{BASE_URL}{ENDPOINT}?key={API_KEY}&q={CITY}&aqi=no"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        print(f"Performing request to Weather API for city {CITY}...")
        location_time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition_text = data["current"]["condition"]["text"]
        location = data["location"]["name"]
        country = data["location"]["country"]

        print(
            f"{location}/{country} {location_time} Weather: "
            f"{temperature} Celsius, "
            f"{condition_text}"
        )
    else:
        print("Failed to retrieve weather data")


if __name__ == "__main__":
    get_weather()
