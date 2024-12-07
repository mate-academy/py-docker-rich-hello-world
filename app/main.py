import json
import os

import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")
CITY = "PARIS"


def get_weather() -> None:
    url = BASE_URL + f"q={CITY}&key={API_KEY}"
    response = requests.get(url).json()
    formatted_json = json.dumps(response, ensure_ascii=False, indent=4)
    print(formatted_json)


if __name__ == "__main__":
    get_weather()
