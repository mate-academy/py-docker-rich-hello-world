import os
import requests

from dotenv import load_dotenv
load_dotenv()


def get_weather() -> str:
    response = requests.get(
        url="https://api.weatherapi.com/v1/current.json",
        params={"q": "Paris", "key": os.environ.get("API_KEY")}
    )
    r_json = response.json()
    r_str = (
        f"{r_json['location']['name']}"
        f"/{r_json['location']['country']} "
        f"{r_json['location']['localtime']} "
        f"Weather: {r_json['current']['temp_c']} Celsius, "
        f"{r_json['current']['condition']['text']}"
    )
    return r_str


if __name__ == "__main__":
    print(get_weather())
