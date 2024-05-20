import os
import requests


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"
    filtering = "Paris&lang=EN"
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError(
            "No API key found. Please set the API_KEY environment variable."
        )

    response = requests.get(f"{url}?q={filtering}&key={api_key}")

    dict_result = response.json()

    weather = (
        f"Weather: {dict_result["current"]["temp_c"]} Celsius, "
        f"{dict_result["current"]["condition"]["text"]}"
    )

    location = (
        f"{dict_result["location"]["name"]}/"
        f"{dict_result["location"]["country"]}"
    )

    time = dict_result["location"]["localtime"]

    result = f"{location} {time} {weather}"
    print("Performing request to Weather API for city Paris...")
    print(result)


if __name__ == "__main__":
    get_weather()
