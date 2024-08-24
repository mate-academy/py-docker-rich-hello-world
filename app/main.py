import requests
import os


URL = "https://api.weatherapi.com/v1/current.json"
LOCATION = "Paris"


def get_weather() -> None:

    api_key = os.getenv("API_KEY")

    if not api_key:
        print("API key not found")
        return

    print(f"Performing request to Weather API for city {LOCATION}...")

    response = requests.get(
        URL,
        {
            "q": LOCATION,
            "key": api_key,
        }
    )

    if response.status_code == 200:
        result = response.json()

        location_data = result["location"]
        current_weather = result["current"]

        city_and_country = (
            f"{location_data['name']}/{location_data['country']}"
        )
        date_and_time = location_data["localtime"]

        temperature = current_weather["temp_c"]
        condition = current_weather["condition"]["text"]
        weather = f"Weather: {temperature} Celsius, {condition}"

        print(f"{city_and_country} {date_and_time} {weather}")

    else:
        response_code_str = f"Response status code {response.status_code}"
        print(f"An error has occurred. {response_code_str}")


if __name__ == "__main__":
    get_weather()
