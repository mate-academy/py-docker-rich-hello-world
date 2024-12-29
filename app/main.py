import os
from typing import Dict

import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

if not API_KEY:
    raise ValueError("API_KEY environment variable not set")


def get_weather(city: str) -> Dict:
    """Fetch current weather data for the specified city."""
    params = {
        "key": API_KEY,
        "q": city,
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def format_weather_output(data: Dict) -> str:
    """Format the weather data into the desired string."""
    location = data["location"]
    current = data["current"]

    city_name = location["name"]
    country = location["country"]
    local_time = location["localtime"]
    temp_c = current["temp_c"]
    condition = current["condition"]["text"]

    return (f"{city_name}/{country} {local_time} "
            f"Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    print(f"Performing request to Weather API for city {CITY}...")
    weather_data = get_weather(CITY)
    print(format_weather_output(weather_data))
