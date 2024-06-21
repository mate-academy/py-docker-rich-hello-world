import requests
import os

BASE_URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"

url = BASE_URL + "key=" + API_KEY + "&q=" + CITY + "&aqi=no"


def get_weather() -> None:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to get weather. Status code: {response.status_code}")
        return

    data = response.json()
    location = data.get("location")
    current = data.get("current")

    city = location.get("name") + "/" + location.get("country")
    time = current.get("last_updated")
    weather = (f"Weather: "
               f"{current.get('temp_c')} "
               f"Celsius, {current.get('condition').get('text')}"
               )

    result = city + " " + time + " " + weather
    print(f"Performing request to Weather API for city Paris...\n{result}")


if __name__ == "__main__":
    get_weather()
