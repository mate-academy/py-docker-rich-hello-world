import os
import requests
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set")
    print("Getting weather for city Paris")
    url = f"{BASE_URL}?key={API_KEY}&q={CITY}&aqi=no"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        city = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        localtime = weather_data["location"]["localtime"]
        temp_c = weather_data["current"]["temp_c"]
        status = weather_data["current"]["condition"]["text"]

        print(f"Country: {country}, city: {city}."
              f" Local time: {localtime}, celsius temperature: {temp_c}, "
              f" weather status: {status}")


if __name__ == "__main__":
    get_weather()
