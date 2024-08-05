import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    print("Performing request to Weather API for city paris...")

    url = (f"http://api.weatherapi.com/v1/"
           f"current.json?key={os.getenv('API_KEY')}&q=Paris")
    response = requests.get(url)

    if response.status_code == 200:
        weather = response.json()

        print(
            f"Paris/France",
            f"{weather["current"]["last_updated"]} "
            f"Weather: "
            f"{weather['current']['temp_c']} "
            f"Celsius, "
            f"{weather["current"]["condition"]["text"]}"
        )


if __name__ == "__main__":
    get_weather()
