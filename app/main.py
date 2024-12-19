import os
import requests

API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

def get_weather() -> None:
    if not API_KEY:
        print("API_KEY environment variable is not set.")
        return

    params = {
        "key": API_KEY,
        "q": CITY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data["location"]
        current = data["current"]

        print(f"Current weather in {location['name']}, {location['country']}:")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Condition: {current['condition']['text']}")
        print(f"Wind: {current['wind_kph']} km/h")
        print(f"Humidity: {current['humidity']}%")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
