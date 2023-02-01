import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "0a293e5d20638517eb1b181a184447fa"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# Bonus Other API
URLO = "https://official-joke-api.appspot.com/random_joke"

# Getting json information from website
def get_joke() -> Dict:
    res = requests.get(URLO)
    return res.json()

def main():
    temp = get_weather("London")
    print(temp)

    # printing the joke information
    joke = get_joke()
    print(joke)

if __name__ == "__main__":
    main()
