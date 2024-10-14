import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
LOCATION = "Paris"


def get_weather() -> None:
    response = requests.get(URL, params={"q": LOCATION, "key": KEY}).json()

    print(f"Current weather in Paris is: "
          f"{response['current']['temp_c']} C, "
          f"humidity: {response['current']['humidity']} %, "
          f"condition: {response['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
