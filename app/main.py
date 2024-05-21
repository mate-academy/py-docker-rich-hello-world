import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    request = requests.get(BASE_URL, params={"key": API_KEY, "q": CITY})

    if request.status_code == 200:
        print(f"Performing request to Weather API for city {CITY}...")

        data = request.json()
        location = data.get("location")
        country = location.get("country")
        time = location.get("localtime")
        current = data.get("current")
        temp = current.get("temp_c")
        condition = current.get("condition").get("text")

        print(f"{CITY}/{country} {time} Weather: {temp} Celsius, {condition}")
    else:
        print("Something went wrong...")


if __name__ == "__main__":
    get_weather()
