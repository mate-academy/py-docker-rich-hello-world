import os

import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def parse_data(weather_data: dict) -> str:
    try:
        city = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        time = weather_data["location"]["localtime"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        result = (f"{city}/{country} {time} "
                  f"Weather: {temperature} "
                  f"Celsius, {condition}")

        return result
    except KeyError as e:
        return f"OOPS, error: {e}"


def get_weather() -> None:
    try:
        response = requests.get(f"{BASE_URL}key={API_KEY}&q={FILTERING}")
        response.raise_for_status()
        weather_data = response.json()
        print(parse_data(weather_data))
    except requests.exceptions.RequestException as e:
        print(f"Problems with fetching data: {e}")


if __name__ == "__main__":
    get_weather()
