import os
import requests
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    URL = f"http://api.weatherapi.com/v1/current.json?key={api_key}"
    FILTERING = "Paris"

    print(f"Performing request to Weather API for city {FILTERING}...")
    response = requests.get(URL + f"&q={FILTERING}")
    data = response.json()

    print(
        f"{data['location']['name']}/"
        f"{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
