import time
import arrow
# file = open("Result_current.txt", "a")         
# t = time.localtime()
# endtime = time.strftime("%H:%M:%S", t)
# file.write ("\nScan End Time: "+str(endtime))
# file.close()
# with open('Result_current.txt') as f:
#     hostname = f.readline().strip()
#     currenttime = f.readline().strip()
#     hostip = f.readline().strip()
#     endtime = f.readline().strip()
#     print ("Hostname: "+ hostname)
#     print ("Scan End Time: "+endtime)
#     currenttime = currenttime.lstrip(": ")
#     print (currenttime)
#     str(timerequired) = str(endtime) - str(currenttime)
#     print (timerequired)

with open('Result_current.txt') as f:
    hostname = f.readline().strip()
    starttime = f.readline().strip()
    enter = arrow.get(starttime, 'HH:mm:ss')
    exit = arrow.now()
    duration = exit - enter
    print(duration)