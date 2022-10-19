from tkinter import *
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
        
#4 : Showing the output (Location, time, rainfall_value, raining/not raining)
if str(rainfall_value()) == 0 :
    print("Location : " + area + ", Current date & time: " + str(now) + ", Rainfall Amount: " + rainfall_value() + ", Status: It is not raining")
else:
    print("Location : " + area + ", Current date & time: " + str(now) + ", Rainfall Amount: " + rainfall_value() + ", Status: It is raining")
    

################################################################################################
# necessary details : Create the application
app = Tk() 
app.title("Weather App")
app.geometry("300x300")
app['background'] = "white"

#Labels, buttons and text
area_text = StringVar()
area_entry = Entry(app, textvariable=area_text, width=45)
area_entry.pack()

search_btn = Button(app, text="Search", width=12, command=getRainfall)
search_btn.pack()

lable_area = Label(app, text="...", width=0, bg='white', font=("bold", 15))
lable_area.place(x=10, y=63)
  
lable_rainfall_value = Label(app, text="...", width=0, bg='white', font=("Helvetica", 15))
lable_rainfall_value.place(x=100, y=95)

rain_situation = Label(app, text="Rain Situation: ", width=0, bg='white', font=("bold", 15))
rain_situation.place(x=3, y=400)
  
lable_situation_rain = Label(app, text="...", width=0, bg='white', font=("bold", 15))
lable_situation_rain.place(x=107, y=400)




# # Dates
# now = datetime.now()
# # date = Label(root, text=now.date, bg='white', font=("bold", 15))
# # date.place(x=100, y=130)

# # # Time
# # hour = Label(root, text=now, bg='white', font=("bold", 15))
# # hour.place(x=10, y=160)



# # Adding the received info into the screen
# # lable_area.configure(text=area)
# # lable_rainfall_value.configure(text=str(rainfall_value()))
# # lable_situation_rain.configure(text=str(situation()))



app.mainloop()


#https://www.geeksforgeeks.org/create-a-gui-for-weather-forecast-using-openweathermap-api-in-python/
#https://www.geeksforgeeks.org/weather-app-in-python-using-tkinter-module/



