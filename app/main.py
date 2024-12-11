import requests
import os

API_KEY = os.getenv("API_KEY")
city = "Paris"


def get_weather() -> None:
    url = (
        f"http:"
        f"//api.weatherapi.com/v1/current.json?key={API_KEY}"
        f"&q={city}&aqi=no"
    )
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['current']['temp_c']}°C")


if __name__ == "__main__":
    get_weather()
