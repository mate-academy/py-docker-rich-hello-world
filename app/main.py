import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("No API key provided")

    response = requests.get(
        BASE_URL,
        params={
            "key": API_KEY,
            "q": CITY,
        },
    )
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Current weather in Paris: "
              f" {weather_data['current']['temp_c']}°C")
    else:
        print(f"Failed to get weather data: {response.status_code}")


if __name__ == "__main__":
    get_weather()
