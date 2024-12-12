import os

import requests


API_KEY = os.getenv("api_key")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    result = requests.get(f"{URL}key={API_KEY}&q={FILTERING}").json()

    city = result["location"]["name"]
    country = result["location"]["country"]
    local_time = result["location"]["localtime"]
    temperature = result["current"]["temp_c"]
    condition = result["current"]["condition"]["text"]

    print("Performing request to Weather API for city Paris...")
    print(
        f"{city}/{country} {local_time} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
