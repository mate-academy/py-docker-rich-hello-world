import os
import requests

API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: No API_KEY found in environment variables.")
        return

    response = requests.get(f"{API_URL}?key={api_key}&q={CITY}")
    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Paris Weather: {temp} °C, {condition}")
    else:
        print("Failed to fetch weather data:",
              response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
