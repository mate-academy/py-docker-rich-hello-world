import requests


def get_weather() -> None:

    api_key = "a5ce67285f3d4da7868112455232704"
    city = "Paris"

    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    )

    if response.status_code == 200:
        data = response.json()
        country = data["location"]["country"]
        current = data["current"]
        date = current["last_updated"]
        temperature = current["temp_c"]
        condition = current["condition"]["text"]
        print(
            f"{city}/{country} {date} "
            f"Weather: {temperature} Celsius, {condition}"
        )

    else:
        print("Failed to fetch weather data")


if __name__ == "__main__":
    get_weather()
