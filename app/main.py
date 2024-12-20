import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = f"http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")
    response = requests.get(URL + f"?key={API_KEY}&q={FILTERING}")
    response.raise_for_status()
    data = response.json()

    print(
        f"{data['location']['name']}/"
        f"{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
