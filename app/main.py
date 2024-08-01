import requests
import json
import os


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("You need to set API_KEY environment variable")
    print("Performing request to weather api for city Paris....")
    res = requests.get(
        f"https://api.weatherapi.com/v1/current.json",
        params={"key": api_key, "q": "Paris", "aqi": "no"}
    )
    if res.status_code == 200:
        content = json.loads(res.content)
    else:
        raise Exception(res.text)

    print(f"{content['location']['country']}/{content['location']['name']} "
          f"{content['location']['localtime']} "
          f"Weather: {content['current']['temp_c']} "
          f"Celsius, {content['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
