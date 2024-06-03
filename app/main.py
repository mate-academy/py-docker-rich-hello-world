import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"
    filtering = "Paris"
    if api_key is None:
        raise ValueError("API_KEY environment variable is not set")
    payload = {
        "key": api_key,
        "q": filtering,
    }
    print("Performing request to Weather API for city Paris...")
    result = requests.get(url, params=payload)
    data = result.json()
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
