import os
import requests
from dotenv import load_dotenv


def get_weather(key: str, city: str) -> None:
    request_url = "http://api.weatherapi.com/v1/current.json"
    parameters = {
        "key": key,
        "q": city,
    }

    response = requests.get(request_url, params=parameters)
    data = response.json()

    if response.status_code == 200:
        return data
    raise Exception(f"{data['error']}: {data['message']}")


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")
    city = "Paris"
    try:
        current_data = get_weather(api_key, city)

        print(f"Current weather in {city}:")
        print(f"Temperature: {current_data['current']['temp_c']}°C")
        print(f"Humidity: {current_data['current']['humidity']}%")
        print(f"Wind speed: {current_data['current']['wind_kph']} km/hour")
        print(f"Cloud: {current_data['current']['cloud']}")
        print(f"UV: {current_data['current']['uv']}")
        print(f"Last update: {current_data['current']['last_updated']} "
              f"by localtime")

    except Exception as e:
        print(e)
