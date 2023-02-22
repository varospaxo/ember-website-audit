import socket
hostip = input ("Enter Host IP: ")
def get_domain_name(ip_address):
  result=socket.gethostbyaddr(ip_address)
  return list(result)[0]
print("Domain name using PTR DNS:")
print(get_domain_name(hostip))
