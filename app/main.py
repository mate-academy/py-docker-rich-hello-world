import os
import urllib.parse
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
params = {
    "key": API_KEY,
    "q": "Paris",
    "agi": "no"
}
URL = "http://api.weatherapi.com/v1/current.json"
url_with_params = f"{URL}?{urllib.parse.urlencode(params)}"


def get_weather() -> None:
    res = requests.get(url_with_params)
    if res.status_code == 200:
        data = res.json()
        name, country = data["location"]["mame"], data["location"]["country"]
        current_data = data["current"]
        last_updated = current_data["last_updated"]
        temp = current_data["temp_c"]
        text = current_data["condition"]["text"]
        print(f"{name}/{country} ")
        print(f"{last_updated} Weather: {temp} Celsius, ")
        print(f"{text}")


if __name__ == "__main__":
    get_weather()
