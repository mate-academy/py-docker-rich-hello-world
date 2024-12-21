import os

import requests
from requests import Response


URL = os.environ.get("URL")
API_KEY = os.environ.get("API_KEY")
FILTERING = os.environ.get("FILTERING")


def get_response() -> Response:
    try:
        response = requests.get(URL + f"?key={API_KEY}&q={FILTERING}")
        response.raise_for_status()
    except requests.ConnectionError:
        raise RuntimeError("There was a problem connecting to the resource.")
    except requests.RequestException:
        raise RuntimeError("An error occurred while making the request.")

    return response


def get_weather() -> None:
    response = get_response()

    if response.ok:
        try:
            location = response.json().get("location")
            current_weather = response.json().get("current")

            city = location.get("name")
            country = location.get("country")
            localtime = location.get("localtime")

            celsius =current_weather.get("temp_c")
            condition = current_weather.get("condition").get("text")
        except (ValueError, KeyError):
            raise ValueError("Failed to decode the JSON response or missing expected data.")
    else:
        print("Failed to retrieve required data.")

    print(f"Performing requests to Weather API for city {FILTERING}...")
    print(f"{city}/{country} {localtime} "
          f"Weather: {celsius} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
