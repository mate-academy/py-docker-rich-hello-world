import os
import requests

API_KEY = os.environ["API_KEY"]

URL = (
    f"http://api.openweathermap.org/data/2.5/weather"
    f"?q=Paris"
    f"&appid={API_KEY}"
    f"&units=metric"
)


def get_weather() -> None:
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]

        print(f"Temperature in Paris: {temperature}°C")
        print(f"Weather description: {weather_description}")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    get_weather()
