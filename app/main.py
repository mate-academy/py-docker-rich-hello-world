import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_weather() -> None:
    KEY = os.getenv("KEY")
    URL = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(URL, params={
        "key": KEY,
        "q": "Paris"
    })

    if response.status_code == 200:
        data = response.json()
        county_city = data["location"]["tz_id"]
        date = data["location"]["localtime"]
        weather = (f"{data['current']['temp_c']} Celsius,"
                   f" {data['current']['condition']['text']}")
        print(f"{county_city} {date}, Weather: {weather}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
