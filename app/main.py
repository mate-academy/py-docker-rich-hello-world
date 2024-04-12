import os
import requests

URL = "https://api.weatherapi.com/v1/current.json?"


def get_weather(city: str) -> None:
    params = {"key": os.getenv("API_KEY"), "q": city.capitalize()}
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()

        country = data.get("location", {}).get("country")
        last_updated = data.get("current", {}).get("last_updated")
        temp_celsius = data.get("current", {}).get("temp_c")
        weather_text = data.get("current", {}).get("condition", {}).get("text")

        print(f"City: {city.capitalize()}/{country}\n"
              f"Last Updated: {last_updated}\n"
              f"Weather: {temp_celsius} °C, {weather_text}")
    else:
        print(f"Could not get weather for {city}, "
              f" status code: {response.status_code}")


if __name__ == "__main__":
    city = "Paris"
    get_weather(city)
