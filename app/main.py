import json
import os
from datetime import datetime

import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        location = f"{data['location']['name']}/{data['location']['country']}"
        local_time = datetime.fromisoformat(data['location']['localtime'])
        temp_celsius = f"{data['current']['temp_c']} Celsius"
        condition = data["current"]["condition"]["text"]

        output = (f"{location} {local_time.strftime('%Y-%m-%d %H:%M')} "
                  f"Weather: {temp_celsius}, {condition}")
        print(output)

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except json.JSONDecodeError:
        print("Error decoding the JSON response")
    except KeyError as e:
        print(f"Missing data in the response: {e}")
    except ValueError as e:
        print(f"Error parsing date: {e}")


if __name__ == "__main__":
    get_weather()
