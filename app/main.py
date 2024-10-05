import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
city = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("API_KEY is not set. Please set it as an environment variable.")
        return

    print("Making a request to the weather API...")

    try:
        response = requests.get(f"{BASE_URL}?q={city}&key={API_KEY}")
        response.raise_for_status()
        weather_data = response.json()

        if "current" in weather_data:
            current_weather = weather_data["current"]
            print(f"Current weather in {city}: ")
            print(f'Temperature: {current_weather["temp_c"]} °C')
            print(f'Condition: {current_weather["condition"]["text"]}')
            print(f'Humidity: {current_weather["humidity"]}%')
            print(f'Wind Speed: {current_weather["wind_kph"]} km/h')
        else:
            print("No current weather data found.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
