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
        location = data["location"]
        current_data = data["current"]
        temp = current_data["temp_c"]
        print(f"{location["name"]}/{location["country"]} ")
        print(f"{current_data["last_updated"]} Weather: {temp} Celsius, ")
        print(f"{current_data["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
