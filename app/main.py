import json
import os
from dotenv import load_dotenv

import requests

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ["API_KEY"]
CITY = "Paris"


def get_weather() -> None:
    url = BASE_URL + f"key={API_KEY}&q={CITY}"
    res = requests.get(url)
    data = res.json()
    formatted_data = json.dumps(data, ensure_ascii=False, indent=4)
    print(formatted_data)


if __name__ == "__main__":
    get_weather()
