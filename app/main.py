import os
import requests

from app.exceptions import MissingAPIKeyError

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise MissingAPIKeyError("No API key provided for Weather API")
    print(f"Performing request to {URL} for {CITY}")

    response_params = {
        "key": API_KEY,
        "q": CITY,
    }

    try:
        response = requests.get(URL, params=response_params)
        response.raise_for_status()
        weather_data = response.json()

        city = weather_data.get(
            "location", {}).get("name", "Unknown city")
        country = weather_data.get(
            "location", {}).get("country", "Unknown country")
        local_time = weather_data.get(
            "location", {}).get("localtime", "Unknown time")
        temp_c = weather_data.get(
            "current", {}).get("temp_c", "value not correct")
        condition_text = (
            weather_data.get("current", {})
            .get("condition", {})
            .get("text", "value not correct")
        )

        print(
            f"Weather in {city},{country} is {condition_text} at {local_time}."
            f"Air temperature: {temp_c} degrees Celsius"
        )

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    get_weather()
