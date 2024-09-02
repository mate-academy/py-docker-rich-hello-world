import requests
import os
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = (f"https://api.weatherapi.com"
           f"/v1/current.json?key={api_key}&q=Paris&aqi=no")

    response = requests.get(url)
    response_json = response.json()
    local = response_json["location"]
    print("Performing request to Weather API for city Paris...")
    print(f"{local['name']}/{local['country']} "
          f"{local['localtime']} Weather: {response_json['current']['temp_c']}"
          f" Celsius, {response_json['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
