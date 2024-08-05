import os
import requests


API_KEY = os.environ["API_KEY"]
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Lviv"


def get_weather() -> None:
    # write your code here
    response = requests.get(
        f"{BASE_URL}?key={API_KEY}&q={CITY}"
    )
    print(response.json())


if __name__ == "__main__":
    get_weather()
