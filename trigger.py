import requests
import json
import urllib2

bet_url = "http://google.co.uk"
print "checking altitude is more than 29500m...\n"
triggered = False # boolean to prevent duplicating bet
altitude_json_link = "http://habitat.habhub.org/habitat/_design/ept/_list/json/payload_telemetry/payload_time?include_docs=true&startkey=[%227830c4b51e021511a9bb8ff5dc1df89a%22]&endkey=[%227830c4b51e021511a9bb8ff5dc1df89a%22,[]]&fields=altitude" # altitude link from Habitat
trigger_json_link = "http://habitat.habhub.org/habitat/_design/ept/_list/json/payload_telemetry/payload_time?include_docs=true&startkey=[%227830c4b51e021511a9bb8ff5dc1df89a%22]&endkey=[%227830c4b51e021511a9bb8ff5dc1df89a%22,[]]&fields=trigger" # trigger link from Habitat
 
while True: # forever
 
    r = requests.get(altitude_json_link) # get the JSON information
    altitude = float(r.json()[-1]["altitude"]) # parse altitude to get a float
    print "The altitude is: " + str(altitude) # print altitude
    
    r = requests.get(trigger_json_link) # get the JSON information
    trigger = str(r.json()[-1]["trigger"]) # parse trigger
    print "The trigger is: " + trigger # print trigger
 
    if altitude >= 29500 and trigger == "True" and triggered == False: # if altitude = 29500m and altitude hasn't already been reached
        response = urllib2.urlopen(bet_url)
        print response.info()


        
        print "Bet Placed! Exiting..."
        triggered = True
        break
