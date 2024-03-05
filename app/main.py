from __future__ import print_function

import os
from dotenv import load_dotenv
import requests


# http://api.weatherapi.com/v1/search.json?key=1a89060c76a14afba95134309242702&q=Paris

URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    work_key = os.environ.get("API_KEY")

    work_params = f"key={work_key}&q={CITY}"

    work_request = requests.get(URL, params=work_params)

    if work_request.status_code != 200:
        print(f"Error request: {work_request.status_code}")

    result = work_request.json()

    test_view = (
        f"Local time: {result['location']['localtime']}, "
        f"temp(C): {result['current']['temp_c']}, "
        f"precipitation: {result['current']['condition']['text']}, "
        f"wind(m/c): {result['current']['wind_mph']}, "
        f"direction wind: {result['current']['wind_dir']}"
    )
    print(test_view)


if __name__ == "__main__":
    get_weather()
