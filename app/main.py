import os
import requests


API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY is not set in environment variables")

    response = requests.get(URL, params={"key": API_KEY, "q": CITY})

    if response.status_code == 200:
        weather_data = response.json()
        current = weather_data['current']
        location = weather_data['location']
        print(f"Weather for city {location['name']}, {location['country']}:")
        print(f"Temperature: {current['temp_c']} Celsius")
        print(f"Condition: {current['condition']['text']}")
    else:
        print("Failed to get weather data")


if __name__ == "__main__":
    get_weather()
