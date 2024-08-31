# Weather App
Overview

This weather app provides current weather conditions and a 5-day weather forecast for any specified city or the user's current location. 

Features

Current Weather: Fetches and displays the current weather for a specified city or the user's location.

5-Day Forecast: Provides a detailed 5-day weather forecast including temperature, humidity, and wind speed.

Recent Searches: Keeps a cache of recently searched cities for quick access.

Info Section: Displays information about the PM Accelerator.

User-Friendly Interface: Simple text-based menu for easy navigation.

Requirements

Python 3.x

requests library for making API calls

geocoder library for fetching user location

An API key from OpenWeatherMap

Installation

Clone the Repository:

git clone <repository-url>

cd <repository-directory>

Install Dependencies:

Make sure you have requests and geocoder installed. You can install them using pip:

pip install requests geocoder

Get OpenWeatherMap API Key:

Sign up at OpenWeatherMap and obtain your API key.

Replace YOUR_API_KEY in the code with your actual API key.

Running the App

Open a terminal or command prompt.

Navigate to the directory where the script is located.

Run the script using Python:

python weather_app.py

Follow the on-screen menu to:

Enter a city name.

Use your current location.

View recent searches.

Access information about the PM Accelerator.

Exit the app.

Code Overview

Functions:

clear_screen(): Clears the console screen.

load_cache(): Loads cached weather data from a JSON file.

save_cache(): Saves weather data to a JSON file.

get_weather_by_city(city): Fetches current weather data for a specified city.

get_forecast_by_city(city): Fetches a 5-day weather forecast for a specified city.

get_weather_by_location(): Fetches current weather data for the user's location.

display_weather(weather_data): Displays current weather information.

display_forecast(forecast_data): Displays the 5-day weather forecast.

display_info(): Displays information about the PM Accelerator.

main(): Main function that runs the app.
