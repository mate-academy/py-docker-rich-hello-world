import os
import requests
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}"
    filtering = "Paris"

    print(f"Performing request to Weather API for city {filtering}...")
    response = requests.get(url + f"&q={filtering}")
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
