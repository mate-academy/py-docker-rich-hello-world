import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_Key")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(
        url=URL,
        params={"key": API_KEY, "q": "Paris"}
    ).json()

    current_temperature = response["current"]["temp_c"]
    current_pressure = response["current"]["pressure_mb"]
    current_humidity = response["current"]["humidity"]

    print("Temperature (in celsius) = " +
          str(current_temperature) +
          "\nAtmospheric pressure (in millibars) = " +
          str(current_pressure) +
          "\nHumidity (in percentage) = " +
          str(current_humidity))


if __name__ == "__main__":
    get_weather()
