import requests
import os


def get_weather() -> str:
    key = os.environ.get("API_KEY")
    url = "https://api.weatherapi.com/v1/current.json"
    payload = {
        "key": key,
        "q": "Paris"
    }
    respond = requests.get(url=url, params=payload)
    if respond.status_code == 200:
        return respond.text
    return "Something went wrong"


if __name__ == "__main__":
    print(get_weather())
