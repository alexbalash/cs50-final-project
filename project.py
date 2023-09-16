import sys
import requests
import time
from retry import retry

def main():
    city = input("Enter a city: ")
    url = make_url(city)
    weather_data = get_weather(url)
    display_forecast_choice(weather_data)

def make_url(city):
    API_URL = "http://api.openweathermap.org/data/2.5/forecast"
    api_key = "4a667b3caefe6915603d5d48f02b50d7"
    city_name = city.title()
    city_name = city_name.replace(" ", "+")
    units = "metric"
    url = f"{API_URL}?q={city_name}&units={units}&appid={api_key}"
    return url

@retry(requests.exceptions.RequestException, tries=3, delay=2)
def get_weather(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_error:
        if response.status_code == 401:
            sys.exit("Unauthorized. Please check your API key.")
        elif response.status_code == 404:
            sys.exit("City not found")
        else:
            sys.exit(f"Problem ({http_error})")
    data = response.json()
    return data

def display_forecast_choice(weather_data):
    forecast_list = weather_data["list"]
    today = time.strftime("%Y-%m-%d", time.localtime())
    seconds_to_tomorrow = 86400
    tomorrow = (time.time() + seconds_to_tomorrow)
    tomorrow = time.strftime("%Y-%m-%d", time.localtime(tomorrow))

    choice = input("Which forecast do you want? (today/tomorrow): ")
    if choice.lower() == "today":
        display_forecast(forecast_list, today, weather_data["city"]["name"])
    elif choice.lower() == "tomorrow":
        display_forecast(forecast_list, tomorrow, weather_data["city"]["name"])
    else:
        print("Invalid choice. Please enter 'today' or 'tomorrow'.")
        display_forecast_choice(weather_data)

def display_forecast(forecast_list, date, city):
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_RED = "\033[91m"

    thunderstorm_emoji = "⛈️"
    drizzle_emoji = "🌧️"
    rain_emoji = "☔"
    snow_emoji = "❄️"
    atmosphere_emoji = "🌫️"
    clear_emoji = "☀️"
    clouds_emoji = "☁️"

    for forecast in forecast_list:
        forecast_date = forecast["dt_txt"].split(" ")[0]
        if forecast_date == date:
            weather_description = forecast["weather"][0]["description"]
            temperature = forecast["main"]["temp"]
            weather_id = forecast["weather"][0]["id"]

            if weather_id < 300:
                emoji = thunderstorm_emoji
            elif weather_id < 400:
                emoji = drizzle_emoji
            elif weather_id < 600:
                emoji = rain_emoji
            elif weather_id < 700:
                emoji = snow_emoji
            elif weather_id < 800:
                emoji = atmosphere_emoji
            elif weather_id == 800:
                emoji = clear_emoji
            else:
                emoji = clouds_emoji

            if temperature < 0:
                temp_color = LIGHT_BLUE
            elif temperature < 20:
                temp_color = YELLOW
            else:
                temp_color = LIGHT_RED

            print(f"{BOLD}{city} - {date:^10}{RESET}", end="   ")
            print(f"{temp_color}{round(temperature)}°C", end="  ",)
            print(f"{BLUE}{emoji}  {weather_description.capitalize()}{RESET}")
            return

if __name__ == "__main__":
    main()
