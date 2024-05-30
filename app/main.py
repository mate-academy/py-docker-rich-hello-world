import os
import requests


API_KEY = os.environ.get("API_KEY")
CITY_NAME = "Paris"
URL = (f"https://api.weatherapi.com/v1/current.json"
       f"?key={API_KEY}&q={CITY_NAME}&aqi=no")


def get_weather() -> None:
    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 1)

        print({
            "city": CITY_NAME,
            "weather_description": weather_description,
            "temperature": temperature
        })
    else:
        response.raise_for_status()


if __name__ == "__main__":
    get_weather()
