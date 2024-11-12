import requests
import os

from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1"
FILTERING = "Paris"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    request = (
        requests
        .get(
            f"{BASE_URL}/current.json?q={FILTERING}&key={API_KEY}"
        ).json())

    location = request["location"]
    current = request["current"]

    print(
        f"{location['name']}/"
        f"{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
