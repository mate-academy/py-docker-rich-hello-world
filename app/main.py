import os

import requests
from dotenv import load_dotenv


load_dotenv()


URL = "http://api.weatherapi.com/v1/current.json"

API_KEY = os.getenv("WEATHER_API_KEY")

CITY = "Paris"


def get_weather() -> None:
    print("Performing request to WeatherAPI for city Paris")
    response = requests.get(f"{URL}?key={API_KEY}&q={CITY}")

    if response.status_code == 200:
        data = response.json()
        print(
            f"{data['location']['name']}/{data['location']['country']} "
            f"{data['current']['last_updated']} "
            f"Weather: {data['current']['temp_c']} Celsius, "
            f"{data['current']['condition']['text']}"
        )
    else:
        print(f"An error occurred {response.status_code}")


if __name__ == "__main__":
    get_weather()
