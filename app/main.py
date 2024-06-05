import os
from datetime import datetime
import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI = "no"
API_KEY = os.environ["API_KEY"]


def get_weather() -> None:
    try:
        print("Performing request to Weather API for city Paris...")

        date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        response = requests.get(
            f"{API_URL}"
            f"?key={API_KEY}&q={CITY}&aqi={AQI}"
        ).json()
        temp = response["current"]["temp_c"]
        condition = response["current"]["condition"]["text"]

        print(f"Paris/France {date_now} Weather: {temp} Celsius, {condition}")

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    get_weather()
