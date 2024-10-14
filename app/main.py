import os
import requests

API_KEY = os.environ["API_KEY"]

CITY = "Paris"
URL = (
    f"http://api.openweathermap.org/data/2.5/weather"
    f"?q={CITY}"
    f"&appid={API_KEY}"
    f"&units=metric"
)


def get_weather() -> None:
    try:
        response = requests.get(URL)
        response.raise_for_status()

        data = response.json()
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]

        print(f"Temperature in Paris: {temperature}°C")
        print(f"Weather description: {weather_description}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
