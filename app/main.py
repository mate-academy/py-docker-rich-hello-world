import os
import requests
from requests.exceptions import (
    ConnectionError,
    JSONDecodeError,
    RequestException
)

from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("API key is missing. Please add it to the environment variables")
        return

    url = f"{URL}q={FILTERING}&key={API_KEY}"
    weather_data = fetch_data(url)
    if weather_data:
        print_weather_data(weather_data)


def fetch_data(url: str) -> dict:
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
