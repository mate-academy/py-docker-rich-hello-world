import os
import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"The current temperature in {CITY} is {temp_c}°C with {condition}.")
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    get_weather()
