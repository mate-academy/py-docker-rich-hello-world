import time

import requests
import json
import os


def get_weather() -> None:
    API_KEY = os.getenv('API_KEY')
    if not API_KEY:
        raise ValueError("You need to set API_KEY environment variable")
    res = requests.get(
        f"http://api.weatherapi.com/v1/current.json?"
        f"key={API_KEY}&q=Paris&aqi=no"
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
