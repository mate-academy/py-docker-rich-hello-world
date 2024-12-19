import requests
import os

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather(city: str, key: str) -> None:
    try:
        response = requests.get(f"{URL}key={API_KEY}&q={CITY}&aqi=no")
        response.raise_for_status()
        data = response.json()
        print(f"{data["location"]["name"]}/{data["location"]["country"]} "
              f"{data["current"]["last_updated"]} "
              f"Weather: {data["current"]["temp_c"]} Celsius, "
              f"{data["current"]["condition"]["text"]}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather(CITY, API_KEY)
