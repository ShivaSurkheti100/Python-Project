## Create Drink Water Notification Reminder App in Python --- <pwd> in terminal gives the path

import time
from plyer import notification ## use < pip install plyer > in terminal 

if __name__ == " __main__" :
    while True:
        notification.notify(
            title = "Please Drink Water Now!!", 
            messagse = "The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men.About 11.5 cups (2.7 liters) of fluids a day for women.", 
            app_icon =  "C:\Users\USER\OneDrive\Desktop\Python\icon.ico",  ## use pwd to copy the path of file
            timeout = 15 
        )
        # time.sleep(6)
        time.sleep(60*60) # for 1 hr 
### use (pythonw .\main.py) in terminal
