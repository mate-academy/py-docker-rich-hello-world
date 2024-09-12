import os
import requests
from dotenv import load_dotenv


load_dotenv()


def get_weather() -> None:

    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Missing API_KEY environment variable")
    else:
        response = requests.get(
            "https://api.weatherapi.com/v1/current.json?q=Paris",
            headers={
                "key": api_key,
            }
        )
        print("Performing request to Weather API for city Paris...")
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        date_time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"{city}/{country} {date_time} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
