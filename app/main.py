import os

import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_weather_data(api_key: str, city: str) -> dict:
    url = (
        f"https://api.weatherapi.com/v1/current.json?"
        f"key={api_key}&q={city}&aqi=yes"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {}


def print_weather_info(data: dict) -> None:
    if not data:
        print("No data to display.")
        return

    location = data["location"]
    current = data["current"]

    print(
        f"Location: {location['name']}, "
        f"{location['region']}, "
        f"{location['country']}"
    )
    print(f"Temperature: {current['temp_c']}°C")
    print(f"Condition: {current['condition']['text']}")
    print(f"Wind: {current['wind_kph']} kph from the "
          f"{current['wind_dir']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Last updated: {current['last_updated']}")


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY not found")
        return

    city = "Paris"
    data = fetch_weather_data(api_key, city)
    print_weather_info(data)


if __name__ == "__main__":
    get_weather()
