import os

import requests
from dotenv import load_dotenv


load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    # write your code here
    print("Performing request to Weather API for city Paris...")
    try:
        response = requests.get(
            URL,
            {
                "q": FILTERING,
                "key": API_KEY
            }
        ).json()
    except requests.RequestException as error:
        print(error)

    city = response.get("location").get("name")
    country = response.get("location").get("country")
    last_updated = response.get("current").get("last_updated")
    degrees = response.get("current").get("temp_c")
    description = response.get("current").get("condition").get("text")

    print(
        f"{city}/{country} {last_updated}"
        f" Weather: {degrees} Celsius, {description}"
    )


if __name__ == "__main__":
    get_weather()
