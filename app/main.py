import requests
import os


def get_weather() -> None:

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set.")

    url = (f"http://api.weatherapi.com/v1/current.json?"
           f"key={api_key}&q=Paris")
    title_request = "Performing request to Weather API for city Paris..."
    result = requests.get(url)
    data_paris = result.json()
    location = (f"{data_paris['location']['name']}/"
                f"{data_paris['location']['country']}")
    local_time = f"{data_paris['location']['localtime']}"
    weather = (f" Weather: {data_paris['current']['temp_c']} "
               f"Celsius, {data_paris['current']['condition']['text']}")
    print(title_request)
    print(location + local_time + weather)


if __name__ == "__main__":
    get_weather()
