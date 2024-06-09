import os
import requests

API_KEY = os.getenv("API_KEY")
CITY_NAME = "Paris"
URL = (f"https://api.weatherapi.com/v1/current.json"
       f"?key={API_KEY}&q={CITY_NAME}&aqi=no")


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("No API key provided")
    response = requests.get(URL)
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Current weather in Paris: "
              f" {weather_data['current']['temp_c']}°C")
    else:
        print(f"Failed to get weather data: {response.status_code}")


if __name__ == "__main__":
    get_weather()
