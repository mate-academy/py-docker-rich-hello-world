import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather(city: str = "Paris") -> requests.Response:
    print(f"Requesting {city} weather from Weather API...")
    params = {"key": API_KEY, "q": city, "aqi": "no"}
    response = requests.get(URL, params=params)

    if response.status_code != 200:
        response.raise_for_status()

    location = response["location"]
    current_temp = response["current"]
    condition = current_temp["condition"]
    print("▼" * 50)
    print(
        f"{location['name']}/{location['country']} {location['localtime']}\n"
        f"Updated at: {current_temp['last_updated']} \n"
        f"Weather: {current_temp['temp_c']} C "
        f"(feels like {current_temp['feelslike_c']} C), {condition['text']}"
    )
    print("▲" * 50)

    return response


if __name__ == "__main__":
    get_weather()
