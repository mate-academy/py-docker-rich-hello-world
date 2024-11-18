import os
import requests
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")

    URL = "http://api.weatherapi.com/v1/current.json"
    PARAMS = {"key": api_key, "q": "Paris"}
    response = requests.get(URL, params=PARAMS)
    data = response.json()

    print(f"Current weather in {data['location']['name']}:")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
