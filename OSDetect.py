# Run As Admin
import nmap
import socket
import os
import subprocess
print('\n-----------Remote OS Detection Started-----------\n')
try:
    with open('Result_current.txt') as f:
        hostname = f.readline().strip()
        print("Detecting Host Operating System for: "+hostname)
    hostip = socket.gethostbyname(hostname)
    nm = nmap.PortScanner()
    machine = nm.scan(hostip, arguments='-O')
    print("OS Type: ", machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['osfamily'])
    print("Detection Accuracy: ", machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['accuracy'])
except IndexError:
    print("Cannot Detect OS for: "+hostname)
print('\n----Scanning Finished----\n')
rawpath = os.getcwd() + "\\SSLCertificate.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])
