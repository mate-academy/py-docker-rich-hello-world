import os

import requests
from requests import RequestException


URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ["API_KEY"]
FILTERING = "Paris"


def get_weather() -> None:
    try:
        response = requests.get(URL + f"?key={API_KEY}&q={FILTERING}")
    except ConnectionError:
        raise ConnectionError(
            "There was a problem connecting to the resource."
        )
    except RequestException:
        raise RequestException("An error occurred while making the request.")

    if response.status_code == 200:
        try:
            city = response.json().get("location").get("name")
            country = response.json().get("location").get("country")
            localtime = response.json().get("location").get("localtime")
            celsius = response.json().get("current").get("temp_c")
            condition = response.json().get(
                "current"
            ).get("condition").get("text")
        except ValueError:
            raise ValueError("Failed to decode the JSON response.")
        except KeyError:
            raise KeyError("Missing expected data in the response.")
    else:
        print("Failed to retrieve required data.")

    print(f"Performing requests to Weather API for city {FILTERING}...")
    print(f"{city}/{country} {localtime} "
          f"Weather: {celsius} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
