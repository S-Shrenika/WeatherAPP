import requests
import geocoder
import os
import json

API_KEY = '63bea33e5947f71ceffd9f377ba0e530' 
CACHE_FILE = 'weather_cache.json'


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_cache():
    """Load cached weather data from a JSON file."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_cache(cache):
    """Save weather data to a JSON file."""
    with open(CACHE_FILE, 'w') as file:
        json.dump(cache, file)

def get_weather_by_city(city):
    """Fetch current weather data for a specified city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_forecast_by_city(city):
    """Fetch 5-day weather forecast for a specified city."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_weather_by_location():
    """Fetch current weather data for the user's current location."""
    g = geocoder.ip('me')
    lat, lng = g.latlng
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather(weather_data):
    """Display current weather information in a user-friendly format."""
    if weather_data.get("cod") != 200:
        print("Error:", weather_data.get("message"))
        return

    city = weather_data['name']
    weather = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"\nCity: {city}")
    print(f"Weather: {weather.capitalize()}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("Stay safe and have a great day!\n")

def display_forecast(forecast_data):
    """Display 5-day weather forecast."""
    if forecast_data.get("cod") != "200":
        print("Error:", forecast_data.get("message"))
        return

    print("\n5-Day Weather Forecast:")
    for entry in forecast_data['list']:
        date = entry['dt_txt']
        weather = entry['weather'][0]['description']
        temperature = entry['main']['temp']
        humidity = entry['main']['humidity']
        wind_speed = entry['wind']['speed']

        print(f"Date: {date}")
        print(f"Weather: {weather.capitalize()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("-" * 30)

def display_info():
    """Display information about the PM Accelerator."""
    print("\nPM Accelerator:")
    print("The Product Manager Accelerator Program is designed to support PM professionals through every stage of their career. From students looking for entry-level jobs to Directors looking to take on a leadership role, our program has helped over hundreds of students fulfill their career aspirations.")
    print("Developed by Shrenika Soma\n")  

def main():
    clear_screen()
    cache = load_cache()

    while True:
        print("Menu:")
        print("1. Enter a city name")
        print("2. Use current location")
        print("3. View recent searches")
        print("4. Info about PM Accelerator")
        print("5. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            city = input("Enter the city name: ")
            weather_data = get_weather_by_city(city)
            forecast_data = get_forecast_by_city(city)
            cache[city] = weather_data
            save_cache(cache)
            display_weather(weather_data)
            display_forecast(forecast_data)
        elif choice == '2':
            weather_data = get_weather_by_location()
            display_weather(weather_data)
            city = weather_data['name']
            forecast_data = get_forecast_by_city(city)
            display_forecast(forecast_data)
        elif choice == '3':
            print("\nRecent Searches:")
            for city in cache.keys():
                print(city)
            print()
        elif choice == '4':
            display_info()
        elif choice == '5':
            print("Exiting the Weather App. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
