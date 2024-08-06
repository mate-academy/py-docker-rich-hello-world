import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("API_KEY not found in environment variables.")
    exit(1)

params = {
    "key": API_KEY,
    "q": "Paris",
    "agi": "no"
}
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    try:
        res = requests.get(URL, params=params)
        res.raise_for_status()

        data = res.json()
        name = data["location"]["name"]
        country = data["location"]["country"]
        current_data = data["current"]
        last_updated = current_data["last_updated"]
        temp = current_data["temp_c"]
        text = current_data["condition"]["text"]

        print(f"{name}/{country}")
        print(f"{last_updated} Weather: {temp} Celsius")
        print(f"{text}")

    except requests.exceptions.RequestException as e:
        print("Failed to retrieve data.")
        print(f"Error: {e}")

    except ValueError:
        print("Failed to parse JSON response.")

    except KeyError as e:
        print(f"Missing key in response data: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_weather()
