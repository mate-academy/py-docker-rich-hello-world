import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"

    if not api_key:
        raise ValueError("API_KEY environment variable not set")

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Current weather for {city}: {weather_data['current']}")
    else:
        print(f"Failed to get weather data: {response.status_code}")


if __name__ == "__main__":
    get_weather()
