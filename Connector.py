import time
import os
import subprocess
hostname = input("Enter the hostname: ")
file = open("./Result.txt", "a")         
file.write(hostname)
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
file.write ("\nScan Start Time: "+str(current_time))
print("Current Time: ", current_time)
file.close()
path_current="./OutputFiles/Result_current.txt"
os.replace("./Result.txt", path_current)
rawpath = os.getcwd() + "\\Ping.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])
