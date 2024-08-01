import time

import requests
import json
import os


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("You need to set API_KEY environment variable")
    res = requests.get(
        f"http://api.weatherapi.com/v1/current.json?"
        f"key={api_key}&q=Paris&aqi=no"
    )
    content = json.loads(res.content)
    print("Performing request to weather api for city Paris....")
    time.sleep(2)
    print(f"{content['location']['country']}/{content['location']['name']} "
          f"{content['location']['localtime']} "
          f"Weather: {content['current']['temp_c']} "
          f"Celsius, {content['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
