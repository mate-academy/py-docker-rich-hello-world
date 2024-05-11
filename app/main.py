import os
import requests

key = os.environ.get("API_KEY")
URL = f"https://api.weatherapi.com/v1/current.json?key={key}&q=Paris"


def get_weather() -> None:
    req = requests.get(URL)
    if req.status_code != 200:
        print("Oops, something went wrong...")
        return

    data = req.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(
        f"{city}/{country} {local_time} Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
