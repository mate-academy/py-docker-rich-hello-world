import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/"
CITY = "Paris"


def get_weather() -> str:
    payload = {"key": API_KEY, "q": CITY}
    get_weather_url = BASE_URL + "current.json"
    response = requests.get(get_weather_url, params=payload)
    print(payload)
    print(get_weather_url)
    if response.status_code == 200:
        data = response.json()
        print(f"{data['location']['name']}/{data['location']['country']} "
              f"{data['location']['localtime']} "
              f"Weather: {str(data['current']['temp_c'])} Celsius, "
              f"{data['current']['condition']['text']}")
    else:
        if response.status_code == 404:
            print("Error 404: Not Found")
        elif response.status_code == 401:
            print("Error 401: Unauthorized")
        elif response.status_code == 500:
            print("Error 500: Internal Server Error")
        else:
            print(f"Error {response.status_code}: Something went wrong")


if __name__ == "__main__":
    get_weather()
