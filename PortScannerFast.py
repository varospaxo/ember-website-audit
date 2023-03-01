# scan a range of port numbers on a host concurrently
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from concurrent.futures import ThreadPoolExecutor
import os
import subprocess
print("\n-----------Remote Port Scanner Started-----------")
# returns True if a connection can be made, False otherwise
def test_port_number(host, port):
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        # set a timeout of a few seconds
        sock.settimeout(3)
        # connecting may fail
        try:
            # attempt to connect
            sock.connect((host, port))
            # a successful connection was made
            return True
        except:
            # ignore the failure
            return False
 
# scan port numbers on a host
def port_scan(host, ports):
    print(f'\nPort Scanning {host}...')
    # create the thread pool
    with ThreadPoolExecutor(len(ports)) as executor:
        # dispatch all tasks
        results = executor.map(test_port_number, [host]*len(ports), ports)
        # report results in order
        for port,is_open in zip(ports,results):
            if is_open:
                print(f'> {host}:{port} open')
                file = open("./PortScannerFast.txt", "a")          
                file.writelines("\n"+str(port))
                file.close()
                
# define host and port numbers to scan

with open('./OutputFiles/Result_current.txt') as f:
    hostname = f.readline().strip()
HOST = hostname
PORTS = range(1024)
# test the ports
port_scan(HOST, PORTS)
path_current="./PortScannerFast.txt"
movepath = "./OutputFiles/PortScannerFast_OP.txt" 
os.replace(path_current, movepath)
print("\n----Scanning Finished----\n")
rawpath = os.getcwd() + "\\Traceroute.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])
