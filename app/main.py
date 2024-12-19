import os
import requests
from dotenv import load_dotenv

load_dotenv()

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    try:
        response = requests.get(URL + f"?key={API_KEY}&q={CITY}")
        response.raise_for_status()
        data = response.json()

        country = data.get("location").get("country")
        localtime = data.get("location").get("localtime")
        celsius = data.get("current").get("temp_c")
        condition = data.get("current").get("condition").get("text")

        print(f"Performing requests to Weather API for city {CITY}...")
        print(f"{CITY}/{country} {localtime} "
              f"Weather: {celsius} Celsius, {condition}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_weather()
