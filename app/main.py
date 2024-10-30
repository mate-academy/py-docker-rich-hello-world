import requests
import os
from dotenv import load_dotenv
load_dotenv()

FORMAT = "json"
URL = "https://api.weatherapi.com/v1/"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:

    response = requests.get(
        URL + f"current.{FORMAT}?key={API_KEY}&q={FILTERING}"
    )
    print(response.status_code, response.json())


if __name__ == "__main__":
    get_weather()
