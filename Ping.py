from pythonping import ping
import socket
hostname = input("Enter hostname: ")
ip_address = socket.gethostbyname(hostname)
print("IP Address: ", ip_address)
response_list = ping(ip_address, size=40, count=10)
if response_list.rtt_avg_ms > 0:
    print ("Host is UP!")
else:
    print("Host is DOWN!")
print("Ping Avg Response Time:", response_list.rtt_avg_ms)
