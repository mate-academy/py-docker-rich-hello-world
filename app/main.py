import os

import requests

from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}
    response = requests.get(URL, params=params)
    data = response.json()

    if response.status_code == 200:

        country = data["location"]["country"]
        last_updated = data["current"]["last_updated"]
        temp_celsius = data["current"]["temp_c"]
        weather_text = data["current"]["condition"]["text"]

        print(
            f"Performing request to Weather API for city Paris... \n"
            f"{CITY}/{country} {last_updated} "
            f"Weather: {temp_celsius} °С, {weather_text}."
        )
    else:
        print(
            f"Status code is {response.status_code}."
        )


if __name__ == "__main__":
    get_weather()
