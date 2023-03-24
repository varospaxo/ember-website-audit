# importing library
import requests
import os
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
			requests.get(url, timeout=2)
			
			# if after putting subdomain one by one url
			# is valid then printing the url
			print(f'[+] {url}')
			f = open("./Subdomain.txt", "a")
			f.write(f'\n[+] {url}')
			f.close()
			
		# if url is invalid then pass it
		except requests.ConnectionError:
			pass
	path_current="./Subdomain.txt"
	movepath = "./OutputFiles/Subdomain_OP.txt" 
	os.replace(path_current, movepath)
	print('\n')

 
#Remove Temp File Save Output File
	
	print('----Scanning Finished----')
	print('-----Scanner Stopped-----')

# main function
if __name__ == '__main__':

	# inputting the domain name
	with open('./OutputFiles/Result_current.txt') as f:
         dom_name = f.readline().strip()
	
print('\n')

	# opening the subdomain text file
with open('Subdomain_names.txt','r') as file:
	
		# reading the file
		name = file.read()
		
		# using splitlines() function storing the
		# list of splitted strings
		sub_dom = name.splitlines()
		
	# calling the function for scanning the subdomains
	# and getting the url
domain_scanner(dom_name,sub_dom)

