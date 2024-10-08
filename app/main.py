import os
import requests
from dotenv import load_dotenv


load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    url_ = requests.get(URL + f"key={API_KEY}&q={FILTERING}")
    if url_.status_code == 200:
        data = url_.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        current_temp_c = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        print("Performing request to Weather API for city Paris...")
        print(
            f"{city}/{country} {localtime} "
            f"Weather: {current_temp_c} Celsius, "
            f"{weather}"
        )


if __name__ == "__main__":
    get_weather()
