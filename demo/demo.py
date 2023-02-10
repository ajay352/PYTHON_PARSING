from datetime import datetime
import os



today = datetime.now()

if today.hour < 12:
    h = "00"
else:
    h = "12"

os.mkdir("/home/wst/Desktop/demo/" + today.strftime("%H:%M:%S")+ h)