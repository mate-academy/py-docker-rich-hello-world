import os

import requests

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city: str = "Paris") -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError(
            "API_KEY is not set. Please provide it as an environment variable"
        )

    url = f"{BASE_URL}?key={api_key}&q={city}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Performing request to Weather API for city {city}...")

        city_name = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"{city_name}/{country} {localtime} "
              f"Weather: {temperature}°C, {condition}")
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    get_weather()
