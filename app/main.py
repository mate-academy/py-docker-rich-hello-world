import os

import requests


API_KEY = os.getenv("api_key")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def parse_weather_data(weather_data: dict) -> str:
    try:
        city = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        local_time = weather_data["location"]["localtime"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        return (
            f"{city}/{country} {local_time} "
            f"Weather: {temperature} Celsius, {condition}"
        )
    except KeyError as e:
        return f"Missing data in response: {e}"


def get_weather() -> None:
    result = requests.get(f"{URL}key={API_KEY}&q={FILTERING}").json()

    print(parse_weather_data(result))


if __name__ == "__main__":
    get_weather()
