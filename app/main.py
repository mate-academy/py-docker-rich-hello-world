import os
from datetime import datetime
import requests


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")

    api_key = os.environ["API_KEY"]
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json"
        f"?key={api_key}&q=Paris&aqi=no"
    ).json()
    temp = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(f"Paris/France {date_now} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
