import os
from typing import Dict, Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def fetch_weather_data(url: str, params: Dict[str, str]) -> Dict[str, Any]:
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")


def process_weather_data(data: Dict[str, Any]) -> str:
    try:
        location_name = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        return (
            f"{location_name}/{country} "
            f"{local_time} Weather: "
            f"{temp_c} Celsius, {weather}"
        )
    except (KeyError, ValueError) as e:
        raise RuntimeError(f"Error processing data: {e}")


def get_weather() -> None:
    try:
        print(f"Start request to Weather API for city {CITY}...")
        data = fetch_weather_data(URL, {"key": API_KEY, "q": CITY})
        result = process_weather_data(data)
        print(result)
    except RuntimeError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_weather()
