import requests
import os

from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    FILTERING = os.getenv("FILTERING")
    print(f"Performing request to Weather API for city {FILTERING}...")
    res = requests.get(
        f"https://api.weatherapi.com/v1/"
        f"current.json?key={API_KEY}&q={FILTERING}"
        f"&aqi=no"
    )
    res = res.json()
    print(f"{res['location']['name']}/{res['location']['country']} "
          f"{res['location']['localtime']} "
          f"Weather: "
          f"{res['current']['temp_c']} Celsius, "
          f"{res['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
