import os

from dotenv import load_dotenv

import requests

load_dotenv()


FILTERING = "Kyiv"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    result = requests.get(URL + f"?key={api_key}&q={FILTERING}")

    if result.status_code == 200:
        weather_data = result.json()
        current_weather = weather_data.get("current", {})

        if current_weather:
            temperature = current_weather.get("temp_c")
            condition = current_weather.get("condition", {}).get("text")
            print(f"Weather in {FILTERING}:")
            print(f"Temperature: {temperature}°C")
            print(f"Weather condition: {condition}")
        else:
            print("Failed to retrieve weather data.")
    else:
        print(f"Request error: {result.status_code}")


if __name__ == "__main__":
    get_weather()
