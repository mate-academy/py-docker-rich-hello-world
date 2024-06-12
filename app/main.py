import requests
import os

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("No API key found. "
                     "Please set the API_KEY environment variable.")


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")
    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING}).json()
    print(
        f"{result["location"]["name"]}/{result["location"]["country"]} "
        f"{result["location"]["localtime"]} "
        f"Weather: {result["current"]["temp_c"]} Celsius, "
        f"{result["current"]["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
