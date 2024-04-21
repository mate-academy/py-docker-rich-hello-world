import os

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"
    url = (f"http://api.weatherapi.com/v1/current.json?key={api_key}&q="
           + str(city))
    response = requests.get(url)
    try:
        data = response.json()
        location = data["location"]
        current = data["current"]
        print(
            f"Weather in {location['name']}, {location['country']}:\n"
            f"Temp: {current['temp_c']} °C\n"
            f"Feels like: {current['feelslike_c']} °C\n"
            f"Wind speed: {current['wind_kph']} kp/h\n"
            f"Condition: {current['condition']['text']}"
        )
    except Exception:
        print("Error. Please enter API_KEY")


if __name__ == "__main__":
    get_weather()
