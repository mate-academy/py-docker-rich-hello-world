import json
import urllib.request
requests


def get_weather(api_key: str) -> None:

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=London"

    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        print(data)


if __name__ == "__main__":
    get_weather("ae04ee4ff49349f0ba8180114241306")
