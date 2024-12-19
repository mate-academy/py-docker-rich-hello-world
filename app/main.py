import os

import requests


FILTERING = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    result = requests.get(URL + f"?key={api_key}&q={FILTERING}")

    print("Performing request to Weather API for city Paris ...")

    if result.status_code == 200:
        weather_data = result.json()
        current_weather = weather_data["current"]
        location = weather_data["location"]

        if current_weather:
            country = location["country"]
            current_time = location["localtime"]
            temperature = current_weather["temp_c"]
            condition = current_weather["condition"]["text"]
            print(f"{FILTERING}/{country} {current_time} Weather: {temperature} Celsius, {condition}")
        else:
            print("Failed to retrieve weather data.")
    else:
        print(f"Request error: {result.status_code}")


if __name__ == "__main__":
    get_weather()
