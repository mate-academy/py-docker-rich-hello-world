import os
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
Q_FILTER = "Paris"


def get_weather() -> None:
    url = f"{BASE_URL}?key={os.getenv('API_KEY')}"
    response = requests.get(url, params={"q": Q_FILTER})

    if response.status_code == 200:
        result = response.json()
        condition = result["current"]["condition"]["text"]
        local_time = result["location"]["localtime"]
        weather = (f"Weather: "
                   f"{result['current']['temp_c']} Celsius, {condition}")
        print(f"Paris/France, {local_time}, {weather}")
    elif response.status_code == 403:
        print("Your API_KEY is invalid or not provided.")
    else:
        print(response.reason)


if __name__ == "__main__":
    get_weather()
