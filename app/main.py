import requests
import os

from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    filtering = os.getenv("FILTERING")
    print(f"Performing request to Weather API for city {filtering}...")
    res = requests.get(
        f"https://api.weatherapi.com/v1/"
        f"current.json?key={api_key}&q={filtering}"
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
