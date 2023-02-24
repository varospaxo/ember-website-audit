import socket
import os
import subprocess
print("\n-----------Reverse DNS Scanner Started-----------\n")
with open('Result_current.txt') as f:
    hostname = f.readline().strip()
    currenttime = f.readline().strip()
    hostip = f.readline().strip()
    
    print ("Domain Name: "+hostname)
    print ("IP Address: "+hostip)
def get_domain_name(ip_address):
  result=socket.gethostbyaddr(ip_address)
  return list(result)[0]
# print("Domain name using PTR DNS:")
print("Reverse DNS address: "+get_domain_name(hostip))
print("\n-----Scanning Finished-----")
rawpath = os.getcwd() + "\\SubdomainRoutes.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])
