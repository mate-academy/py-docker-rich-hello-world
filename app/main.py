import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Start request to Weather API for city {CITY}...")
    res = requests.get(URL, params={"key": API_KEY, "q": CITY})

    if res.status_code == 200:
        data = res.json()
        location_name = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]

        print(
            f"{location_name}/{country} "
            f"{local_time} Weather: {temp_c} Celsius, {weather}"
        )
    else:
        print(
            f"status code {res.status_code} something went wrong {res.reason}"
        )


if __name__ == "__main__":
    get_weather()
