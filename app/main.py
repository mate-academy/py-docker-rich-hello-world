import os
import requests


URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"
COUNTRY = "France"
API_KEY = os.getenv("API_KEY")

def get_weather() -> None:

    response = requests.get(URL + f"q={CITY}&key={API_KEY}")
    data = response.json()

    last_updated = data["current"]["last_updated"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(f"{CITY}/{COUNTRY} {last_updated} "
          f"Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
