import os

import requests

FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    payload = {"key": API_KEY, "q": FILTERING}
    response = requests.get(URL, params=payload)

    if response.status_code == 200:
        data = response.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        print(
            f"{city}/{country} {time}, "
            f"Weather: {temperature} Celsius, {weather}"
        )
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    get_weather()
