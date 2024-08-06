import os
import requests


API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city: str) -> None:
    try:
        res = requests.get(URL, params={"key": API_KEY, "q": city})

        data = res.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]

        print(
            f"{city}/{country} "
            f"{time} "
            f"Weather: {temperature} celsius, "
            f"{weather}"
        )
    except requests.RequestException as e:
        raise RuntimeError(f"Exception message: {e}")
    except (KeyError, ValueError) as e:
        raise RuntimeError(f"Exception message: {e}")


if __name__ == "__main__":
    get_weather("Paris")
