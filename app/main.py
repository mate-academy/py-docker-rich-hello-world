import os
import requests

API_KEY = os.environ.get("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    res = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": "Paris"
        }
    )
    data = res.json()
    if res.status_code == 200:
        location_name = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        print(f"Performing request to Weather API for city {location_name}...")
        print(f"{location_name}/{country} "
              f"{local_time} Weather: {temp_c} Celsius, {weather}")
    else:
        print(f"status code {res.status_code} means that {res.text}")


if __name__ == "__main__":
    get_weather()
