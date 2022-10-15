import requests
import json
from datetime import datetime

base_url = "https://api.data.gov.sg/v1/environment/rainfall?"

#1: Extract current rainfall data as current time into JSON file

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

############# Retrieving station_id ####################
#i : Get list of stations in Singapore
api_data = response.content
output = json.loads(api_data)
stations_data = output['metadata']['stations']

#ii:  Get specific station device_id by filtering through the list
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
            break
    else:
        return("Error. Location not found")
        
############# Retrieving rainfall_value ####################
#i : Based on device_id, go into the list of dictionary to get the rainfall value
#First level - Getting the list into dictionary so that we can access to 'Readings'#
get_readings = output['items'][0]
#Change 'readings' to a list where rainfall value can be extracted#
read = get_readings['readings']

#ii : Get rainfall_value by filtering through the list
def rainfall_value():
# initializing required key
    req_key = 'value'
# initializing filter key
    fil_key = 'station_id'
# initializing filter val 
    fil_val = str(device_id())
    
    for rainfall_value in read:
        if rainfall_value[fil_key] == fil_val:
            return(str(rainfall_value[req_key]))
            break
    else:
        return("NIL")
        
#4 : Showing the output (Location, time, rainfall_value, raining/not raining)
if str(rainfall_value()) == '0' :
    print("Location : " + area + ", Current date & time: " + str(now) + ", Rainfall Amount: " + rainfall_value() + ", Status: It is not raining")
elif str(rainfall_value()) == 'NIL':
    print("Location : " + area + ", Current date & time: " + str(now) + ", Rainfall Amount: " + rainfall_value() + ", Status: Unknown Status")
else:
    print("Location : " + area + ", Current date & time: " + str(now) + ", Rainfall Amount: " + rainfall_value() + ", Status: It is raining")    