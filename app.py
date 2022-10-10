# from tkinter import *
import requests
import json
from datetime import datetime
import pandas as pd


base_url = "https://api.data.gov.sg/v1/environment/rainfall?"

#1: Extract current rainfall data into JSON file

## Getting current date and time ###
date = datetime.today().strftime('%Y-%m-%d')
#current time
now = datetime.now()
h = now.strftime("%H")
m = now.strftime("%M")
s = now.strftime("%S")

#2: Getting URL response
complete_url = base_url + "date_time=" + date + "T" + h + "%3A" + m + "%3A" + s
response = requests.get(complete_url)

#In case, if API Data is down:# If status code is 200, site is okay. Other than that, it is down
status_code = response.status_code
if status_code != 200:
    print("Uh oh, there was an issue accessing the data or check if site is down. Please try again later")

#3: Streamlining data 

#Asking user for area in-question#
area = input("What area will you like to check?: ")

#(i) - User input area name , retrieve list of stations in SG
api_data = response.content
output = json.loads(api_data)
stations_data = output['metadata']['stations']


#(ii): Get station device_id by filtering through the list
def device_id():
#Getting value from this key -
    req_key = 'device_id'  
# Basing it off filter key
    fil_key = 'name'
# Input name by user must match to filter value
    fil_val = area
# Filter key's value from other key by using loop
    for device_id in stations_data:
        if device_id[fil_key] == fil_val:
            return(str(device_id[req_key]))

#3: User to input area name to get rainfall value:
def rainfall_value():

#User input
# area = input("Which area will you like to check: ")

# #Filter area = name, retrieve device_id (stations)
# for i in range(len(response_dict)):
#     if area in response_dict[i]['metadata']['stations']['name']:
#         try:
#             print(f"yes")except KeyError:
#             print("nil")



















# def station_id():
#     for i in range(len(response_dict)):
#         if response_dict[i]['metadata']['stations']['name'] == area:
#             print(f"yes")         
 

        
# print(station_id())
    


#Filter station_id, retrieve rainfall value

#output : if rainfall value > 0 == raining. Else, not raining

#Filtering through list to get value:
# output = ""

# def station_id():
    
# if area == 


















# def getWeather():
#     api = complete_url
#     city = area_value.get()
#     complete_url = base_url + "date_time=" + date + "T" + h + "%3A" + m + "%3A" + s
#     response = requests.get(complete_url)
# 	weather_info = response.json()


# def showWeather(): 
#     # Get city name from user from the input field (later in the code)
#     area = area_value.get()
#     # API url
#     complete_url = base_url + "date_time=" + date + "T" + hour + "%3A" + min + "%3A" + sec
#     # Get the response from fetched url
#     response = requests.get(complete_url)
#     # changing response from json to python readable 
#     weather_info = response.json()

#  #-----------Storing the fetched values of weather of a city
 
#     rainfall = int(weather_info['metadata'][''] )                                   
    
 

# print("Location: ${area_value}" + "Time:", hour , min, sec, + "Rainfall Amount:" + rainfall)
 



 
# #assigning Values to our weather varaible, to display as output
         
#         weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
#     else:
#         weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
