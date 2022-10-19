from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
# from pywebio.platform.flask import webio_view
from datetime import datetime
import requests
import json
import pandas as pd
import random
# from flask import Flask, send_from_directory


# app = Flask(__name__)

def main():
    put_markdown('## Rainfall Service Started')

    def good_words():
        sentences = ["Do not be angry with the rain; it simply does not know how to fall upwards", 'Can you believe this weather?', 'Without rain, there is no life', 'he sun after the rain is much more beautiful than the sun before the rain.']
        return(random.choice(sentences))

    put_text(good_words())

    area = input("What's the area you will like to check?")

    base_url = "https://api.data.gov.sg/v1/environment/rainfall?"
    date = datetime.today().strftime('%Y-%m-%d')
    #current time
    now = datetime.now()
    h = now.strftime("%H")
    m = now.strftime("%M")
    s = now.strftime("%S")

    complete_url = base_url + "date_time=" + date + "T" + h + "%3A" + m + "%3A" + s
    response = requests.get(complete_url)

    #In case, if API Data is down:# If status code is 200, site is okay. Other than that, it is down
    # status_code = response.status_code
    # if status_code != 200:
    #     print("Uh oh, there was an issue accessing the data or check if site is down. Please try again later")


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
        
    def situation():
        if str(rainfall_value()) == '0' :
            return("Let's go out! It's not raining 😎")
        elif str(rainfall_value()) == 'NIL':
            return("Unknown Status")
        else:
            return("Movie & Pizza? It's raining 😢")

    ##############################################################
    if str(rainfall_value()) == 'NIL':
        put_table([
        ["Name of Area:", "Date", "Rainfall Value", "Raining/Not Raining"],
        [area, date, str(rainfall_value()), str(situation())]
        ])
    else:
        put_table([
        ["Name of Area:", "Date", "Rainfall Value", "Raining/Not Raining"],
        [area, date, str(rainfall_value()) + "mm", str(situation())]
        ])
################ CSV Table ############
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
    "Name of Area": [area],
    "Date and Time": [now],
    "Rainfall Value" : [str(rainfall_value())],
    "Raining/Not Raining" : [str(situation())]
    }
    #load data into a DataFrame object:

    df = pd.DataFrame(data)
    # df.set_index('name of area', inplace=True) 
    df.to_csv("area_file.csv", sep ='\t', index=False)
    area_file = open('area_file.csv', 'rb').read()
    
    put_file('area_data.csv', area_file, 'Click to download')      


if __name__ == '__main__':
    start_server(main, port=8080, debug=True)


## Run image as container
#    $ docker run -p 8080:8080 python-docker
## Running in browser on http://localhost:8080

