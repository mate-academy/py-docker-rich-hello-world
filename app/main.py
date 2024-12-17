import os
import requests
from requests.exceptions import (
    ConnectionError,
    JSONDecodeError,
    RequestException
)


URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ["API_KEY"]
FILTERING = os.environ.get("FILTERING", "Paris")


def get_weather() -> dict:
    url = f"{URL}q={FILTERING}&key={API_KEY}"
    weather_data = fetch_data(url)
    print_weather_data(weather_data)


def fetch_data(url: str) -> dict:
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except ConnectionError as exc:
        print(f"Connection failed: {exc}")
    except JSONDecodeError as exc:
        print(f"Decoding failed: {exc}")
    except RequestException as exc:
        print(f"Request failed: {exc}")


def print_weather_data(data: dict) -> None:
    try:
        print(
            f'{data["location"]["name"]}/{data["location"]["country"]} '
            f'{data["current"]["last_updated"]} '
            f'Weather: {data["current"]["temp_c"]} '
            f'Celsius, {data["current"]["condition"]["text"]}'
        )
    except KeyError as exc:
        print(f"No such key: {exc}")


if __name__ == "__main__":
    get_weather()
