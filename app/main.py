import os
import requests


URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather(city: str, api_key: str) -> None:
    try:
        response = requests.get(f"{URL}q={city}&key={api_key}")
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data {e}")

    try:
        print(
            f"{data["location"]["name"]}/{data["location"]["country"]} "
            f"{data["current"]["last_updated"]} "
            f"Weather: {data["current"]["temp_c"]} Celsius, {data["current"]["condition"]["text"]}"  # noqa
        )
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    get_weather(FILTERING, API_KEY)
