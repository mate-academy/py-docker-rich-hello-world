import os
import requests


def get_weather() -> None:
    if api_key := os.getenv("API_KEY"):
        print("Performing request to Weather API for city Paris ...")

        url = "http://api.weatherapi.com/v1/"
        api_method = "current.json"
        city = "Paris"

        response = requests.get(f"{url}{api_method}?key={api_key}&q={city}")

        response_location = response.json()["location"]
        response_current = response.json()["current"]

        tz_id = response_location["tz_id"]
        localtime = response_location["localtime"]
        temperature_celsius = response_current["temp_c"]
        condition_text = response_current["condition"]["text"]

        print(
            f"{tz_id} {localtime} "
            f"Weather: {temperature_celsius} "
            f"Celsius, {condition_text}"
        )
    else:
        print(
            "You should to add API_KEY "
            "(ex. docker run -e API_KEY=key_number docker-weather-api)"
        )


if __name__ == "__main__":
    get_weather()
