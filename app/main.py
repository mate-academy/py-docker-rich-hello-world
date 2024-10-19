from os import getenv, environ

import requests

API_KEY = getenv("API_KEY")
API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(f"{API_URL}?key={API_KEY}&q={CITY}")
    response.raise_for_status()

    data = response.json()

    location = data["location"]
    country = location["country"]

    current = data["current"]
    local_time = location["localtime"]
    current_temp = current["temp_c"]
    current_conditions = current["condition"]["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(
        f"{CITY}/{country} {local_time} "
        f"Whether: {current_temp} Celsius, "
        f"{current_conditions}"
    )


if __name__ == "__main__":
    get_weather()
