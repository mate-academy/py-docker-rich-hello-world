import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not found.")

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }
    res = requests.get(BASE_URL, params=params)
    if res.status_code == 200:
        data = res.json()
        location = data["location"]

        print(f"Taking weather information about {CITY} from Weather API")
        print(
            f"Location: {location["name"]}, {location["country"]}\n"
            f"Time: {location["localtime"]}\n"
            f"Temperature: {data["current"]["temp_c"]} Celsius degrees"
        )
    else:
        print("Error:", res.status_code, res.text)


if __name__ == "__main__":
    get_weather()
