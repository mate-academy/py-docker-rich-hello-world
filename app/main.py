import json
import os

import requests
import urllib.parse

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": os.environ.get("API_KEY"),
        "q": FILTERING,
    }

    print(
        json.dumps(
            requests.get(url=URL + urllib.parse.urlencode(params)).json(),
            indent=2,
        )
    )


if __name__ == "__main__":
    get_weather()
