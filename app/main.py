import os
import requests


API_KEY = os.environ.get("API_KEY")

city = "Paris"

BASE_URL = (f"https: //api.weatherapi.com/v1/current.json"
            f"?key={API_KEY}&q={city}&aqi=no")


def get_weather() -> None:
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        weather_data = response.json()
        print(f'{city}: {weather_data["current"]["last_updated"]}. '
              f'Weather - {weather_data["current"]["condition"]["text"]}. '
              f'Temperature: {weather_data["current"]["temp_c"]} C')
    else:
        print(f"Failed to get weather data. Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
