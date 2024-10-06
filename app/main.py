import os
import requests

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": "Paris"}
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        response_data = response.json()
        localtime = response_data["location"]["localtime"]
        temp_c = response_data["current"]["temp_c"]
        condition = response_data["current"]["condition"]["text"]
        print("Performing request to Weather API for city Paris...")
        print(
            f"Paris/France {localtime} "
            f"Weather: {temp_c} Celsius, {condition}"
        )
    else:
        print(f"{response.status_code}", end=" ")
        error = response.json().get("error")
        if error:
            print(error["message"])


if __name__ == "__main__":
    get_weather()
