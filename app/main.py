import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = API_URL
    params = {
        "key": api_key,
        "q": CITY,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        location = f"{data['location']['name']}/{data['location']['country']}"
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(
            f"{location} {local_time} Weather: {temp_c} Celsius, {condition}.")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch weather data: {e}")
    except KeyError as e:
        print(f"Unexpected response structure: {e}")


if __name__ == "__main__":
    get_weather()
