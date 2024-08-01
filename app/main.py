import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    res = requests.get(URL, params={"key": API_KEY, "q": FILTERING})

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
