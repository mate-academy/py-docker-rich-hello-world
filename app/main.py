import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?key="
FILTERING = "Paris"


def get_weather() -> None:

    result = requests.get(URL + API_KEY + f"&q={FILTERING}&aqi=no")
    if result.status_code == 200:
        data = result.json()
        location = data["location"]
        current_data = data["current"]
        temp = current_data["temp_c"]
        current_weather = (
            f"{location['name']}/{location['country']} "
            f"{current_data['last_updated']} Weather: {temp} Celsius, "
            f"{current_data['condition']['text']}"
        )
        print(current_weather)


if __name__ == "__main__":
    get_weather()
