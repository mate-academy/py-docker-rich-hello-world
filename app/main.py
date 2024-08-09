import os
import requests


def get_weather(api_key: str, city: str = "Paris") -> None:
    url = (
        f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()

        weather_data = response.json()

        location_name = weather_data['location']['name']
        country = weather_data['location']['country']
        localtime_epoch = weather_data['location']['localtime_epoch']
        temperature = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']

        print(
            f"{location_name}/{country} "
            f"{localtime_epoch} "
            f"Temperature: {temperature} "
            f"Celsius, {condition}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Failed to get weather data: {e}")

    except ValueError:
        print("Failed to parse JSON from the response.")

    except KeyError as e:
        print(f"Missing key in the JSON data: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set.")
    else:
        get_weather(api_key)
