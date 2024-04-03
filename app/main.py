import os
import requests

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> dict | None:
    payload = {
        "q": CITY,
        "key": API_KEY
    }
    response = requests.get(BASE_URL, params=payload)

    if response.status_code == 200:
        return response.json()["current"]

    print(f"Error: Failed to fetch weather data. "
          f"Status code: {response.status_code}")

    return None


def print_weather(weather: dict) -> None:
    print("Weather in Paris:")
    print(f"Temperature: {weather["temp_c"]}°C")
    print(f"Condition: {weather["condition"]["text"]}")
    print(f"Wind: {weather["wind_kph"]} km/h")


if __name__ == "__main__":
    if not API_KEY:
        print(
            "Error: Weather API key is missing. "
            "Set WEATHER_API_KEY environment variable."
        )
    else:
        weather = get_weather()
        print_weather(weather)
