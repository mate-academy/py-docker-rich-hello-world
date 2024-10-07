import os
import requests


API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    print("API_KEY is not set. Please set the API_KEY environment variable.")
    exit(1)
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    """Fetch and display the current weather for the specified city."""
    try:
        response = requests.get(f"{URL}?key={API_KEY}&q={CITY}&aqi=no")
        response.raise_for_status()

        data = response.json()

        location = data.get("location")
        current_weather = data.get("current")

        if location and current_weather:
            local_time = location.get("localtime")
            country = location.get("country")
            temperature = current_weather.get("temp_c")
            condition = current_weather.get("condition", {}).get("text", "N/A")

            print(f"Weather update for {CITY}, {country}: \n"
                  f"Local Time: {local_time}\n"
                  f"Temperature: {temperature} °C\n"
                  f"Condition: {condition}")
        else:
            print("Weather data is not available.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
