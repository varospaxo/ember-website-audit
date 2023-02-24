# importing library
import requests
import datetime
import time
# function for scanning subdomains
def domain_scanner(domain_name,sub_domnames):
	print('-----------Subdomain Scanner Started-----------\n')
	
	# loop for getting URLs
	for subdomain in sub_domnames:
	
		# making url by putting subdomain one by one
		url = f"https://{subdomain}.{domain_name}"
		
		# using try catch block to avoid crash of
		# the program
		try:
		
			# sending get request to the url
			requests.get(url)
			
			# if after putting subdomain one by one url
			# is valid then printing the url
			print(f'[+] {url}')
			
		# if url is invalid then pass it
		except requests.ConnectionError:
			pass
	print('\n')
	print('----Scanning Finished----')
	print('-----Scanner Stopped-----')

# main function
if __name__ == '__main__':

	# inputting the domain name
	with open('Result_current.txt') as f:
         dom_name = f.readline().strip()
	
print('\n')

	# opening the subdomain text file
with open('hehe.txt','r') as file:
	
		# reading the file
		name = file.read()
		
		# using splitlines() function storing the
		# list of splitted strings
		sub_dom = name.splitlines()
		
	# calling the function for scanning the subdomains
	# and getting the url
domain_scanner(dom_name,sub_dom)
