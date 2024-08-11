import requests
from dotenv import load_dotenv
import os

API_KEY = os.getenv("WEATHER_API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    load_dotenv()
    response = requests.get(f"{URL}?key={API_KEY}&q={FILTERING}")

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        raise RuntimeError(
            f"Failed to get data, error code: {response.status_code}"
        )


if __name__ == "__main__":
    get_weather()
