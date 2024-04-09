import requests
import os

CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json?"


def get_weather() -> None:
    response = requests.get(
        URL + f"key={os.getenv('API_KEY')}&q={CITY}"
    )
    if response.status_code == 200:
        data = response.json()
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]
        wind_speed_km = data["current"]["wind_kph"]
        wind_speed_mile = data["current"]["wind_mph"]
        print(f"City: {CITY}\n"
              f"Temperature: {temp_c} °C ({temp_f} °F)\n"
              f"Wind Speed: {wind_speed_km} km ({wind_speed_mile} mile)")
        return
    print(f"Could not get weather, status code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
