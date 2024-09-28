import requests
import os
from dotenv import load_dotenv


load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }
    response = requests.get(URL, params=params)

    print(f"Performing request to Weather API for city {CITY}")
    if response.status_code == 200:
        data = response.json()
        city = f"{data['location']['name']}/{data['location']['country']}"
        localtime = data["location"]["localtime"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"{city} {localtime} Weather: {temp} Celsius, {condition}")
    else:
        print(response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
