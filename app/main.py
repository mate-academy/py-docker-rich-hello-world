import os

from dotenv import load_dotenv

import requests


load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    CITY = "Paris"
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    url = f"{BASE_URL}?key={api_key}&q={CITY}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        current_weather = weather_data.get("current", {})

        if current_weather:
            temperature = current_weather.get("temp_c")
            condition = current_weather.get('condition', {}).get('text')
            print(f"Weather in {CITY}:")
            print(f"Temperature: {temperature}°C")
            print(f"Weather condition: {condition}")
        else:
            print("Failed to retrieve weather data.")
    else:
        print(f"Request error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
