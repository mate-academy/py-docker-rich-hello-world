import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather() -> None:
    try:
        res = requests.get(
            f"https://api.weatherapi.com/v1/current.json?"
            f"key={API_KEY}&q=Paris&aqi=no"
        )
        res.raise_for_status()  # Raise an exception for HTTP errors
        data = res.json()
        print(
            f"The current weather in Paris is "
            f"{data['current']['temp_c']} Celsius"
        )
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
