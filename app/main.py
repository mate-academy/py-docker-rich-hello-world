import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set or empty")

    params = {
            "key": API_KEY,
            "q": CITY
        }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        city = weather_data['location']['name']
        temp_c = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        print(f"The weather in {city} {current_time}: {temp_c}°C, {condition}.")

    else:
        print(response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
