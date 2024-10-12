import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    result = requests.get(URL + f"q={FILTERING}&key={API_KEY}")
    if result.status_code == 200:
        city = result.json()["location"]["name"]
        country = result.json()["location"]["country"]
        date_time = result.json()["location"]["localtime"]
        temp = result.json()["current"]["temp_c"]
        weather = result.json()["current"]["condition"]["text"]

        print(f"Performing request to Weather API for city {city}...")
        print(f"{city}/{country} {date_time} Weather: {temp} Celsius, {weather}")
    else:
        print(f"Temporary problems with connection to Weather API."
              f"{result.status_code}")

if __name__ == "__main__":
    get_weather()
