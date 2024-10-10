import os

import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY not found in environment variables.")

    try:
        url = f"{BASE_URL}?key={API_KEY}&q={CITY}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        temperature = data["current"]["temp_c"]
        weather_description = data["current"]["condition"]["text"]

        print(f"The current temperature in {CITY} is {temperature}°C.")
        print(f"Weather description: {weather_description}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    get_weather()
