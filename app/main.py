import os
import requests

# Constants
BASE_URL = "http://api.weatherapi.com/v1/current.json"
DEFAULT_CITY = "Paris"


def get_weather() -> None:
    """
    Fetches and prints weather information for a city using the Weather API.
    """
    # Get API key from environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise EnvironmentError("API_KEY environment variable is not set.")

    # Get city from user input (default is Kyiv)
    city = input(
        f"Enter the city name (default: {DEFAULT_CITY}): "
    ) or DEFAULT_CITY

    # Prepare the request URL
    url = f"{BASE_URL}?key={api_key}&q={city}"

    try:
        # Send the GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Extract and print weather information
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {city}: {temperature}°C, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
