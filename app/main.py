from dotenv import load_dotenv
import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    load_dotenv()

    api_key = os.getenv("API_KEY")

    result = requests.get(
        URL + "?key=" + api_key + "&q=" + CITY
    )

    if result.status_code == 200:
        result = result.json()
        city = result["location"]["name"]
        country = result["location"]["country"]
        localtime = result["location"]["localtime"]
        temperature_by_celsius = result["current"]["temp_c"]
        weather_condition = result["current"]["condition"]["text"]

        print(
            f"The weather in {city}({country}) "
            f"at {localtime} is {weather_condition}. "
            f"Temperature is {temperature_by_celsius} degrees Celsius"
        )
    else:
        result.raise_for_status()


if __name__ == "__main__":
    get_weather()
