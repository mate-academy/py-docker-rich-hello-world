import os

from dotenv import load_dotenv

import requests

load_dotenv()

api_key = os.environ.get("API_KEY")


def get_weather() -> None:
    city = "Paris"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    try:
        response.status_code == 200
        weather = response.json()
        print(
            f"Weather in {weather['current']['last_updated']} {city}: "
            f"{weather['current']['temp_c']}˚C, "
            f"{weather['current']['condition']['text']}"
        )
    except requests.exceptions.ConnectionError:
        print("API key not provided.")


if __name__ == "__main__":
    get_weather()
