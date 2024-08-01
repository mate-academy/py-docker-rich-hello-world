import os
import requests

KEY = os.environ["API_KEY"]
BASE_URL = "http://api.weatherapi.com/v1/"
CITY = "London"


def get_weather() -> None:
    response = requests.get(
        f"{BASE_URL}current.json?key={KEY}&q={CITY}",
    )
    print(response.json())


if __name__ == "__main__":
    get_weather()
