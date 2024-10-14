import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
LOCATION = os.getenv("city")
CURRENT_PARAMS = {"q": LOCATION, "key": KEY}


def get_weather() -> None:
    response = requests.get(URL, params=CURRENT_PARAMS).json()

    print(f"Current weather in {LOCATION} is: "
          f"{response['current']['temp_c']} C, "
          f"humidity: {response['current']['humidity']} %, "
          f"condition: {response['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
