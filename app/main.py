import os
import requests


def get_weather(query: str) -> None:
    print("Performing request to Weather API for city Paris...")
    api_key = os.environ.get("API_KEY", )
    if api_key is None:
        raise EnvironmentError("You should set your API key")
    responce = requests.post(
        f"https://api.weatherapi.com/v1/current.json?"
        f"key={api_key}&q={query}&aqi=no/"
    )
    if responce.status_code == 200:
        current = responce.json()["current"]
        location = responce.json()["location"]
        print(f"{location['tz_id']} {current['last_updated']} "
              f"Weather: {current['temp_c']} Celsius!!!")
    else:
        raise EnvironmentError("Your API key is invalid or "
                               "servise doesn't work -__-lake8")


if __name__ == "__main__":
    get_weather("Paris")
