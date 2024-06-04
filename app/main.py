import os
import requests


def get_weather(api_key: str, city: str = "Paris") -> None | str:
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        raise Exception(
            f"Error fetching weather data: "
            f"{response.status_code} - {response.text}"
        )


def format_weather_data(weather_data: str) -> str:
    location = weather_data["location"]
    current = weather_data["current"]
    city = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    temperature = current["temp_c"]
    condition = current["condition"]["text"]
    formatted_data = (
        f"{city}/{country} {localtime} "
        f"Weather: {temperature} "
        f"Celsius, {condition}"
    )
    return formatted_data


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable not set")

    print("Performing request to Weather API for city Paris:")
    weather_data = get_weather(api_key)
    formatted_weather_data = format_weather_data(weather_data)
    print(formatted_weather_data)
