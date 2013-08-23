import time
import requests

text_file_path = ""
initialised = False
the_trigger = "altitude 30000m reached! I'm in space!"
trigger_word_1 = "altitude"
trigger_word_2 = "space"
trigger_word_3 = "reached"

altitude_json_link = "http://habitat.habhub.org/habitat/_design/ept/_list/json/payload_telemetry/payload_time?include_docs=true&startkey=[%22c3d528cd4dcc690f7c7d5e7a014ba642%22]&endkey=[%22c3d528cd4dcc690f7c7d5e7a014ba642%22,[]]&fields=altitude"

def check_trigger():
    while True:
        with open(text_file_path, "r") as f:
        
            for line in f: # for each line in text file
        
                if str(the_trigger) in line and initialised == False: # if the line contains what is required and it hasn't already...
                    initialised = True
                    print "Yes! in line!"
                    requests.post("http://requestb.in/16t4rn21")
                    break
                elif str(trigger_word_1) in line and initialised == False or str(trigger_word_2) in line and initialised == False or str(trigger_word_3) in line and initialised == False:
                    initialised = True
                    print "Yes! in line!"
                    requests.post("http://requestb.in/16t4rn21")
                    break 
                else:
                    print "not yet"

def get_altitude():
    r = requests.get(altitude_json_link) # get altitude from URL
    altitude = float(r.json()[-1]["altitude"]) # parse altitude
    return altitude
    

while True:
    altitude = get_altitude() # check altitude
    if altitude >= 25000 and altitude_reached == False: # if alt above 25km, we know it's safe to check for message
        check_trigger() # check for message
        altitude_reached = True
 
    time.sleep(1)
    print altitude
 
    if initialised == True:
        f.close()
        break
