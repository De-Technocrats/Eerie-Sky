#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, time
from colorama import init, Fore

init(autoreset=True)

print(Fore.BLUE + """
         /~````````````````````````````````~\ 
        (  ██▀ ██▀ █▀▄ █ ██▀   ▄▀▀ █▄▀ ▀▄▀   )
        (  █▄▄ █▄▄ █▀▄ █ █▄▄   ▄██ █ █  █    )
         \_~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_/ 
              Creator: TheNooB4 & DrEerie
                Team: De-Technocrats             """)

time.sleep(1)
print(Fore.RED+"NOTE: EerieSky will ask about location name to give good response.Please make sure to enter spell correctly!!")
time.sleep(1.1)

# Function to display loading animation
def display_loading_animation():
    chars = '|/-\\||'
    for char in chars:
        print(f"\rLoading...{char}", end=" ", flush=True)
        time.sleep(0.5)
# Display loading animation
display_loading_animation()

print("") #to move input prompt on next line of loading.
#inputing data
city = input(Fore.LIGHTGREEN_EX+"Enter the city-name: ")
country = input(Fore.LIGHTGREEN_EX+"Enter the county-name: ")
#Capitalize the first letter of each word
city = city.capitalize()
country = country.capitalize()

# API url and key
url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = '3947edb38e0696350a30dbfacc782bd5'

# Parameters for API call
params = {'q': f'{city},{country}',
          'appid': api_key,
          'units': 'metric'}
# API call
response = requests.get(url, params=params)

# Get response in json format
data = response.json()

# Check weather parameters
if data['cod'] == 200:  # Check if response is successfully
    # Display weather information
    print(f""" {Fore.LIGHTMAGENTA_EX}
    Here's the information about the weather in {city} , {country}:
    
            last update: {time.ctime(data['dt'])}
            Temperature: {data['main']['temp']}°C
            Feels like: {data['main']['feels_like']}°C
            Humidity: {data['main']['humidity']} %
            Wind Speed: {data['wind']['speed']} m/s
            Wind direction: {data['wind']['deg']}°
            Pressure: {data['main']['pressure']} hPa
            Visibility: {data['visibility']} m
            Longitude: {data['coord']['lon']}°
            Latitude: {data['coord']['lat']}°
            Clouds: {data['clouds']['all']} %
            Description: {data['weather'][0]['description']} """)
    print(f"""{Fore.LIGHTCYAN_EX}
    Here's the information about time in {city} , {country}:
    
            Timezone in GMT: {data['timezone'] / 3600} hours
            Current time: {time.ctime(data['dt'])}
            Sunrise: {time.ctime(data['sys']['sunrise'])}
            Sunset: {time.ctime(data['sys']['sunset'])}
            day length in sec: {data['sys']['sunset'] - data['sys']['sunrise']} seconds
            day length in hours: {(data['sys']['sunset'] - data['sys']['sunrise']) / 3600:.3f} hours
            day length in minutes: {(data['sys']['sunset'] - data['sys']['sunrise']) / 60:.3f} minutes
         
            """)

    if 'rain' in data:
        print(f"Rain dates: {data['rain']}")  # dates of rainfall

else:  # Error occurred
    print(f"{Fore.RED}Error {data['cod']}: {data['message']}")
    print(Fore.RED + "Please try again! "
                     "Make sure you have entered the correct city and country name.Also check your internet connection."
                     " If you have entered the correct city and country name, then try again later."
                     " If the problem persists, please contact the developer.")

print(Fore.LIGHTYELLOW_EX + "Thank you for using EerieSky! Have a nice day! ")
