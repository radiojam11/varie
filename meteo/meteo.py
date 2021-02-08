###############################################################################
# Wifi Network Connection Example
#
# Created: 2016-07-27 11:00:55.020628
#
################################################################################

import requests
import json
from time import sleep
# type here your API key!
# or you can use ours...however, if our calls quota is exceded 
# the example won't work :(
api_key = "XXXXX qui la tua key"
        
while(True):
        
    for i in range(3):
        try:
            print("Trying to connect...")
            # to get weather info you need to specify a correct api url
            # there are a lot of different urls with different functions
            # they are all documented here http://openweathermap.org/api
            
            # let's put the http query parameters in a dict
            params = {
                "APPID":api_key,
                "q":"Grosseto"   # <----- here it goes your city
            }
            
            # the following url gets weather information in json based on the name of the city
            url="http://api.openweathermap.org/data/2.5/weather"
            # url resolution and http protocol handling are hidden inside the requests module
            response = requests.get(url,params=params)
            # if we get here, there has been no exception, exit the loop
            break
        except Exception as e:
            print(e)
    
    
    try:
        # check status and print the result
        if response.status_code==200:
            print("Success!!")
            print("-------------")
            # it's time to parse the json response
            js = json.loads(response.content)
            # super easy!
            print("Weather:",js["weather"][0]["description"],js["main"]["temp"]-273,"degrees")
            print("-------------")
    except Exception as e:
        print("ooops, something very wrong! :(",e)
    
    sleep(60)
