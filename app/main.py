import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

PARAMS = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather() -> None:
    response = requests.get(URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()

        print(f"Performing request to Weather API for city {CITY}...")

        city = data.get("location")["name"]
        country = data.get("location")["country"]
        localtime = data.get("location")["localtime"]
        temperature = data.get("current")["temp_c"]
        condition = data.get("current")["condition"]["text"]

        print(
            f"{city}/{country} {localtime} "
            f"Weather: {temperature} Celsius, {condition}"
        )

    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
