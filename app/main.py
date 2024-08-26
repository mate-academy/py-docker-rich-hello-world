import os

import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.weatherapi.com/v1/current.json"
FILTER = "Paris"


def get_weather() -> None:
    weather_response = requests.get(
        BASE_URL, params={"key": os.getenv("API_KEY"), "q": FILTER}
    )

    if weather_response.status_code == 200:
        print(weather_response.content)
    elif weather_response.status_code == 401:
        print("API key has not been provided or is not valid.")
    elif weather_response.status_code == 403:
        print("API key is disabled or you don't have access to the resource.")
    else:
        print(f"There is an error. Try fixing this: "
              f"{weather_response.content}")


if __name__ == "__main__":
    get_weather()
