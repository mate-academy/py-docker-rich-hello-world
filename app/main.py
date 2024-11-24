import os

import requests


def get_weather(api_key: str, city: str) -> requests.Response | None:
    url = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(url=url, params={"key": api_key, "q": city})
    if response.status_code == 200:
        return response.json()
    return None


def main() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("Api key environment not set")
    try:
        weather = get_weather(api_key=api_key, city="Paris")
        print(
            f"Weather in Paris: {weather["current"]["temp_c"]}°C, "
            f"{weather["current"]["condition"]["text"]}"
        )
    except Exception as e:
        print(f"Failed to get weather: {e}")


if __name__ == "__main__":
    main()
