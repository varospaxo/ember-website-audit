# import socket
# import ssl
# import datetime


# class ssl_check():

#     def __init__(self, hostname):
#         print ("%s"%(hostname))
#         # https://www.w3schools.com/python/python_datetime.asp
#         ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
#         context = ssl.create_default_context()
#         # to wrap a socket.
#         conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=hostname,)
#         conn.settimeout(10.0)
#         conn.connect((hostname, 443))
#         ssl_info = conn.getpeercert()
#         print(ssl_info)
#         Exp_ON=datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
#         Days_Remaining= Exp_ON - datetime.datetime.utcnow()
#         print ("Expires ON:- %s\nRemaining:- %s" %(Exp_ON,Days_Remaining))
#         print ("----------------------------------")


# domains = ['google.com', 'yahoo.com', 'facebook.com', "twitter.com"]

# I am using map function to iterate through the list.

# map(ssl_check, domains)
import ssl
import socket
import datetime
import boto3

client = boto3.client("ses", region_name="us-east-1")

print(f"Check SSL Certificate Expiry Date\n")

##opening file
host = input("Enter Hostname: ")
# port= input ("Enter Port (80, 8080, 443): ")
port='443'
try:
            print(f"\nChecking certifcate for server {host}")
            context = ssl.create_default_context()
            with socket.create_connection((host, port)) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    certificate = ssock.getpeercert()
                certExpires = datetime.datetime.strptime(
                    certificate["notAfter"], "%b %d %H:%M:%S %Y %Z"
                )
                daysToExpiration = (certExpires - datetime.datetime.now()).days
                print(f"Expires on: {certExpires} in {daysToExpiration} days")
                ##preparing mailbody
                mailbody = (
                    "Server name: "
                    + host
                    + ", expires in "
                    + str(daysToExpiration)
                    + " days."
                )

except:
            print(f"error on connection to Server or incorrect port selected, {host}")

        ##sending ses email
print(f"\nCert check complete!")