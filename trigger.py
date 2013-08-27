import requests
import json
import urllib2

trigger_url = ""
 
triggered = False 
altitude_json_link = "" # altitude link from Habitat
trigger_json_link = "" # trigger link from Habitat
 
while True: # forever
 
    r = requests.get(altitude_json_link) # get the JSON information
    altitude = float(r.json()[-1]["altitude"]) # parse altitude to get a float
    print "The altitude is: " + str(altitude) # print altitude
    
    r = requests.get(trigger_json_link) # get the JSON information
    trigger = str(r.json()[-1]["trigger"]) # parse trigger
    print "The trigger is: " + trigger # print trigger
 
    if altitude >= 29800 and trigger == "True" and triggered == False: # if altitude = 30000m and altitude hasn't already been reached
        response = urllib2.urlopen(trigger_url)
        print response.info()
        print "Bet Placed! Exiting..."
        triggered = True
        break
