import requests


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"
    filtering = "Paris&lang=EN"
    key = "c1b6dc2b885248bb9ac115114242005"
    response = requests.get(f"{url}?q={filtering}&key={key}")
    dict_result = response.json()

    weather = (
        f"Weather: {dict_result.get("current")["temp_c"]} Celsius, "
        f"{dict_result.get("current").get("condition")["text"]}"
    )

    location = (f"{dict_result.get("location")["name"]}"
                f"/{dict_result.get("location")["country"]} ")

    time = f"{dict_result.get("location")["localtime"]}"

    result = f"{location} {time} {weather}"
    print("Performing request to Weather API for city Paris...")
    print(result)


if __name__ == "__main__":
    get_weather()
