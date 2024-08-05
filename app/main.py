import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.environ["API_KEY"]
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        f"{BASE_URL}?key={KEY}&q={CITY}",
    )

    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    current_data = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]
    print(
        f"{city}/{country} "
        f"{current_data} "
        f"Weather: {temperature} Celsius, "
        f"{weather}"
    )


if __name__ == "__main__":
    get_weather()
