# Level 5 - Modules
# 5.1 - Installing & Using Modules
# Each Spam Van needs to download the daily meny from a website
# Python request module can do this

# Introducing modules
# Modules are code libraries that contain functions we can call from our code. They make our lives easier by implementing the hard stuff for us.
# examples are random and math modules
import random

ticket = random.randint(1, 1000)
print(ticket)

import math

answer = math.sqrt(3)
print(answer)

# Installing Modules With Pip
# Some modules are not pre-installed with Python.
# An example of this is the request module.
# The request module doesn't come pre-installed with Python, so we'll have to install it. Pip is a package manager that will install modules for us.
# pip install - installs python modules for us
# pip install requests  --  Do this in the bash

# The HTTP Request Response Cycle
# spam_van.py will ask for data from a web server.
# Our request for data from the server is called an HTTP request
# The server responds with data in a format called JSON.

# Using JSON to Format and Share Data
# JSON is a standard way to format and share data
# JSON uses a collection of keys and values, which look like Python dictionaries, or JS and Ruby Objects.
# example of JSON data
# [
#     {
#         "price": "3.00",
#         "name": "Omelet",
#         "desc": "Yummy"
#     },
#     {
#         "price": "5.75",
#         "name": "Burrito",
#         "desc": "Breakfast Burrito"
#     },
#     {
#         "price": "4.50",
#         "name": "Waffles",
#         "desc": "Belgian waffles with syrup"
#     }
# ]
# When we get it in Python, JSON uses a collection of keys and values, which look just like Python dictionaries and lists
# It is essentially a list of dictionaries

# How would JSON be used to story our menu
# What if we wanted to store more info about a menu item -- its name, description, and price?
# We could do this witha  dictionary that has keys for name, description, and price
first_item  = {'name': 'Spam n Eggs',
              'desc': 'Two eggs with Spam',
              'price': 2.50}

second_item = {'name': 'Spam n Jam',
              'desc': 'Biscuit with Jam with Spam',
              'price': 3.50}

print(first_item['name'],  first_item['price'])
print(second_item['name'], second_item['price'])

# Since we are going to have a lot of these menu items(which are dictionaries), it makes sense to store them in a list.
menu_items = [first_item, second_item]
# to get the first item
print(menu_items[0]['name'], menu_items[0]['price'], menu_items[0]['desc'])
print(menu_items[1]['name'], menu_items[1]['price'], menu_items[1]['desc'])

# We can also store the menu items directly into our list instead of creating variables for them first.
menu_items = [{'name': 'Spam n Eggs',
               'desc': 'Two eggs with Spam',
               'price': 2.50},
              {'name': 'Spam n Jam',
               'desc': 'Biscuit with Jam with Spam',
               'price': 3.50},
              {'name': 'Spam n Ham',
               'desc': 'Ham & Spam',
               'price': 4.50}]
# Now our format is the same as the JSON data we'll get from our request.
# Instead of hard-coding this menu, let's get it from our HTTP request.

# Getting Today's Menu
# Requesting and printing today's menu (steps)
# 1. Import the module so we can use it for requests
import requests
# 2. Call request.get() with our URL
my_request = requests.get('http://go.codeschool.com/spamvanmenu')
# 3. Call json method to get the response in JSON format
menu_list = my_request.json()

print("Today's Menu:")
for item in menu_list:
    print(item['name'], ': ', item['desc'].title(), ', $',
          item['price'], sep='')
# NOTE str.title() returns a copy of the string in which the first character of all words are capitalized

# Challenge 5.4 - Weather Request
# OpenWeatherMap.org provides an API for looking up weather forecasts. We'll use our previously installed requests module to connect to their website's API and download the daily current temperature for our circus in Orlando, FL.
# The url we will use is "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=2de143494c0b295cca9337e1e96b00e0"
# The first part connects to their API: http://api.openweathermap.org/data/2.5/weather. Then you can see we set q=Orlando,fl for the location, units=imperial for Fahrenheit, and finally we have an appid=... which you can sign up for on their website if you have an app that's using their service.
import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=2de143494c0b295cca9337e1e96b00e0"
request = requests.get(url)

weather_json = request.json()

print(weather_json)

weather_main = weather_json['main']

temp = weather_main['temp']

print("The Circus's current temperature is ", temp)

# 5.5 - Creating Modules
# Lots of Code in One File is a Problem
# If we put all of our code in one file, it's going to get really hardto read and maintain.
# Up until now, the spam_van.py file is responsible for:
# printing the menu
# taking orders
# sales reports
# accessing the menu from the network

# A script containing definitions is a module and can be imported by a script or another module.
# We will separate orders, menu, and sales into their own Modules
# A script containing definities is a modules, and can be imported by another script or module.
# As long as the modules are in the same directory, we can import them into the spam_van.py script like so...
import orders
import menu
import sales

# See the files span_van.py and orders.py to see the structure of the modules and it in action.
# I will still take notes abut how this works from the video below.
# Figuring out What Goes in the Orders Module

# In order to call the functions that are within a module from a script, you need to add module_name.function_name() instead of just the function_name()

# Challenge 5.6 - Creating a Module for Weather
# Assume that circus.py will control all of our circus functionality, like showing the schedule, selling tickets, and displaying the weather forecast. In order to keep things more organized, let's create a separate module for the weather. We'll do that by moving our weather-specific code to weather.py and then calling that code from our circus.py script.

# See the circus.py and weather.py files inside the weather directory.
