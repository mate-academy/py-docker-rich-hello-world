import os
from datetime import datetime

import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": "Paris",
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        location = f"{data['location']['name']}/{data['location']['country']}"
        local_time = datetime.fromisoformat(data['location']['localtime'])
        temp_celsius = f"{data['current']['temp_c']} Celsius"
        condition = data["current"]["condition"]["text"]
        output = (f"{location} {local_time.strftime('%Y-%m-%d %H:%M')} "
                  f"Weather: {temp_celsius}, {condition}")
        print(output)


if __name__ == "__main__":
    get_weather()
