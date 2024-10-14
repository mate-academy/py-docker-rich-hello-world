import requests
import os


def get_weather(api_key: str) -> None:
    city = "Paris"
    base_url = f"http://api.weatherapi.com/v1/current.json?key=" f"{api_key}&q={city}"
    response = requests.get(base_url)
    weather = response.json()

    if response.status_code == 200:
        print(
            f"{weather["location"]["name"]}/"
            f"{weather["location"]["country"]} "
            f"{weather["location"]["localtime"]} "
            f"Weather: {weather["current"]["temp_c"]} "
            f"Celsius, {weather["current"]["condition"]["text"]}"
        )
    else:
        "There is no data about weather"


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    get_weather(api_key)
