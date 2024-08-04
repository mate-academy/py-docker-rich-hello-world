import os
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


def get_weather() -> None:
    res = requests.get(URL, params=params)
    if res.status_code == 200:
        data = res.json()
        name, country = data["location"]["name"], data["location"]["country"]
        current_data = data["current"]
        last_updated = current_data["last_updated"]
        temp = current_data["temp_c"]
        text = current_data["condition"]["text"]
        print(f"{name}/{country} ")
        print(f"{last_updated} Weather: {temp} Celsius, ")
        print(f"{text}")

    else:
        print("Failed to retrieve data.")
        print(f"Status code: {res.status_code}")
        print(f"Reason: {res.reason}")


if __name__ == "__main__":
    get_weather()
