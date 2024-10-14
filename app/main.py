import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
LOCATION = os.getenv("city")


def get_weather() -> None:
    current_param = {"q": LOCATION, "key": KEY}
    response = requests.get(URL, params=current_param).json()

    print(f"Current weather in {LOCATION} is: "
          f"{response['current']['temp_c']} C, "
          f"humidity: {response['current']['humidity']} %, "
          f"condition: {response['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
