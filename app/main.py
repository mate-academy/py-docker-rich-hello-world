import os
import requests

CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        raise EnvironmentError("API_KEY environment variable not set.")

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"Weather in {CITY}: {weather.capitalize()}, {temp}°C")
    else:
        print(f"Error: {response.json()['message']}")


if __name__ == "__main__":
    get_weather()
