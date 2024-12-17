import os

import requests
from requests import (
    ConnectionError,
    JSONDecodeError,
    RequestException
)


URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ["API_KEY"]
FILTERING = os.environ.get("SEARCH_CITY", "Paris")


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")

    try:
        response = requests.get(
            URL,
            {
                "q": FILTERING,
                "key": API_KEY
            }
        )
        response.raise_for_status()
        weather_data = response.json()
        weather_data_output(weather_data)
    except ConnectionError as exc:
        print(f"Error: A Connection error occured {exc}")
    except JSONDecodeError as exc:
        print(f"Error: Couldn’t decode the text into json {exc}")
    except RequestException as exc:
        print(f"Error: There was an ambiguous exception that"
              f" occurred while handling your request. {exc}")


def weather_data_output(weather_data: dict) -> None:
    city = weather_data["location"]["name"]
    country = weather_data["location"]["country"]
    last_updated = weather_data["current"]["last_updated"]
    degrees = weather_data["current"]["temp_c"]
    description = weather_data["current"]["condition"]["text"]

    print(
        f"{city}/{country} {last_updated}"
        f" Weather: {degrees} Celsius, {description}"
    )


if __name__ == "__main__":
    get_weather()
