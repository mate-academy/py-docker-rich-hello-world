import requests
import os
from dotenv import load_dotenv


script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

load_dotenv(os.path.join(parent_dir, ".env"))

URL = "https://api.weatherapi.com/v1/forecast.json"
CITY = "Paris"


def get_weather() -> None:
    key = os.getenv("API_KEY", "")
    response = requests.get(f"{URL}?q={CITY}&key={key}")
    if response.status_code == 200:
        print(response.text)
    else:
        print("Key is not provided or invalid")


if __name__ == "__main__":
    get_weather()
