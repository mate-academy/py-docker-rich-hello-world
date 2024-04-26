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
    ).json()

    city = result.get("location").get("name")
    country = result.get("location").get("country")
    localtime = result.get("location").get("localtime")
    temperature_by_celsius = result.get("current").get("temp_c")
    weather_condition = result.get("current").get("condition").get("text")

    print(
        f"The weather in {city}({country}) "
        f"at {localtime} is {weather_condition}. "
        f"Temperature is {temperature_by_celsius} degrees Celsius"
    )


if __name__ == "__main__":
    get_weather()
