import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    req = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": CITY,
        },
    )

    if req.status_code == 200:
        response_current = req.json().get("current")

        print(
            f"Temperature in {CITY}: {response_current.get('temp_c')}°C"

        )
    else:
        print(
            f"Status code: {req.status_code}"
        )


if __name__ == "__main__":
    get_weather()
