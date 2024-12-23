import os
import requests

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": "Paris",
            "aqi": "no"
        }
    )
    response.raise_for_status()
    data = response.json()
    print(
        f"{data["location"]["name"]} {data["location"]["country"]}"
        f" {data["location"]["localtime"]} {data["current"]["temp_c"]} C"
    )


if __name__ == "__main__":
    get_weather()
