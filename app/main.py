import os

from dotenv import load_dotenv

import requests


load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    city = "Paris"
    base_url = "http://api.weatherapi.com/v1/current.json"

    url = f"{base_url}?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        current_weather = weather_data.get("current", {})

        if current_weather:
            temperature = current_weather.get("temp_c")
            condition = current_weather.get('condition', {}).get('text')
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Weather condition: {condition}")
        else:
            print("Failed to retrieve weather data.")
    else:
        print(f"Request error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
