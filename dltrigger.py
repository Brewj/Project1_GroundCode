import time
import sys
 
text_file_path = "" # location path of your text file
initialised = False
the_trigger = "" # the trigger message coming from the payload
trigger_url = "" # URL to be loaded
 
while True:
 
    with open(text_file_path, "r") as f: # open text file
        
        for line in f: # for each line in text file
        
            if str(the_trigger) in line and initialised == False: # if the line contains what is required and it hasn't already...
                initialised = True
                requests.get(trigger_url)
                print "Yes! Trigger in line"
                break
            else: # if not in line
                print "not yet" 
    time.sleep(1) # delay to keep while loop stable
 
    if initialised == True: # if trigger has been executed
        break # end program
