import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    data = {
        "key": os.getenv("API_KEY"),
        "q": "Paris"
    }
    response = requests.get(url=URL, params=data)

    if response.status_code == 200:
        data = response.json()
        country = data["location"]["country"]
        city = data["location"]["name"]
        date = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        description = data["current"]["condition"]["text"]
        print(
            f"{country}/{city} {date}"
            f"Weather: {temperature} Celsius, {description}"
        )

    else:
        print(f"Error(status code: {response.status_code})")


if __name__ == "__main__":
    get_weather()
