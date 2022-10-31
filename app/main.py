import os

import requests

from dotenv import load_dotenv

load_dotenv()

API_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    res = requests.get(
        API_URL,
        params={
            "key": API_KEY,
            "q": CITY
        }
    ).json()

    print(f"City: {CITY}; Current temperature: {res['current']['temp_c']} Celsius; "
          f"Local time: {res['location']['localtime']}; "
          f"Condition: {res['current']['condition']['text']};")


if __name__ == "__main__":
    get_weather()
