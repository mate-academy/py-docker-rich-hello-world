import os

import requests
from dotenv import load_dotenv
from requests.exceptions import (
    ConnectionError,
    JSONDecodeError,
    RequestException
)


load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.environ["API_KEY"]


def get_weather() -> None:
    """
    Get weather data from the API and print it.
    """
    url = f"{URL}q={FILTERING}&key={API_KEY}"
    weather_data = fetch_data(url)
    if weather_data:
        print_weather_data(weather_data)


def fetch_data(url: str) -> dict:
    """
    Fetch data from the API.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except ConnectionError as exc:
        print(f"Connection error: {exc}")
    except JSONDecodeError as exc:
        print(f"JSON decoding error: {exc}")
    except RequestException as exc:
        print(f"Request error: {exc}")
    return {}


def print_weather_data(data: dict) -> None:
    """
    Print weather data.
    """
    try:
        location = data["location"]
        current = data["current"]
        print(
            f'{location["name"]}, {location["country"]} '
            f'({current["last_updated"]})\n'
            f'Temperature: {current["temp_c"]}°C\n'
            f'Condition: {current["condition"]["text"]}'
        )
    except KeyError as exc:
        print(f"Missing key: {exc}")


if __name__ == "__main__":
    get_weather()
