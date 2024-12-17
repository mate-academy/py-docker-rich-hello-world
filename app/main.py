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
    except ConnectionError as exs:
        print(f"Connection failed: {exs}")
    except JSONDecodeError as exs:
        print(f"Decoding failed: {exs}")
    except RequestException as exs:
        print(f"Request failed: {exs}")


def print_weather_data(data: dict) -> None:
    try:
        print(
            f"{data["location"]["name"]}/{data["location"]["country"]} "
            f"{data["current"]["last_updated"]} "
            f"Weather: {data["current"]["temp_c"]} "
            f"Celsius, {data["current"]["condition"]["text"]}"
        )
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    get_weather()
