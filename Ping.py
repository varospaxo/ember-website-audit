from pythonping import ping
import socket
import os
import subprocess

hostname = ""
print("\n-----------Host Service Detection-----------\n")
try:
    with open('Result_current.txt') as f:
        hostname = f.readline()
        print ("Host status for: "+ hostname)
        ip_address = socket.gethostbyname(hostname.strip())
        file = open("Result_current.txt", "a")         
        file.write("\n"+ip_address)
        file.close()
    print("IP Address: ", ip_address)
    response_list = ping(ip_address, size=40, count=10)
    if response_list.rtt_avg_ms > 0:
        print ("Host is UP!")
    else:
        print("Host is DOWN!")
    print("Ping Avg Response Time:", response_list.rtt_avg_ms)
except socket.gaierror:
    print("Hostname unavailable!")
    exit()
print("\n----Scanning Finished----\n")
rawpath = os.getcwd() + "\\PortScannerFast.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])

