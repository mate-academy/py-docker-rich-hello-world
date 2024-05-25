import requests
import os

from dotenv import load_dotenv


load_dotenv()


API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Kyiv"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
    if response.status_code == 200:
        data = response.json()
        location_name = data["location"]["name"]
        location_country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        print(
            f"{location_name}/{location_country} {localtime} "
            f"Weather: {temperature} Celsiush {weather}"
        )
    else:
        print(f"Failed to fetch weather data: code {response.status_code}")


if __name__ == "__main__":
    get_weather()
