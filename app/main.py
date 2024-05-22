import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city: str = "Paris") -> None:
    print(f"Performing request to Weather API for city {city}...")
    params = {
        "key": API_KEY,
        "q": city,
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            print("City not found or API request failed.")
        else:
            weather = {
                "city": data["location"]["name"],
                "region": data["location"]["region"],
                "country": data["location"]["country"],
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
            }
            print(
                f"City: "
                f"{weather['city']}, {weather['region']}, {weather['country']}"
            )
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Condition: {weather['condition']}")
    else:
        print("City not found or API request failed.")


if __name__ == "__main__":
    get_weather()
