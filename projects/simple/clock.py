import time
from datetime import datetime

while True:    
    now = datetime.now()
    print ("%02d/%02d/%04d %02d:%02d:%02d" % (now.month,now.day,now.year,now.hour,now.minute,now.second), end='\r')
    time.sleep(0.1)
