import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city: str = "Paris") -> None:
    if not API_KEY:
        raise ValueError("No API key provided.")

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
            print(f"City: {weather['city']}, "
                  f"{weather['region']}, "
                  f"{weather['country']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Condition: {weather['condition']}")
    else:
        print("City not found or API request failed.")


if __name__ == "__main__":
    get_weather()
