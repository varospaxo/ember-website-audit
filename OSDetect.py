# Run As Admin
import nmap
import socket
hostname = input("Enter hostname: ")
hostip = socket.gethostbyname(hostname)
nm = nmap.PortScanner()
machine = nm.scan(hostip, arguments='-O')
print("OS Type: ", machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['osfamily'])
print("Detection Accuracy: ", machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['accuracy'])