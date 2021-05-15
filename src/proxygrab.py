import requests 
from bs4 import BeautifulSoup
import sys
from colorama import Fore, Style


# Set the Url vars


class Proxy:
	def __init__(self, url, option):

		self.url = url 
		self.option = option 
		
		


	def status_code_check(self):
		# Request the URL and print the status code
		get_url = requests.get(self.url) 

		# Check conditional status code
		check = get_url.status_code

		if check == 200:
			print("Request status code 200")
		elif check == 400:
			print("Bad Request Error")
			sys.exit()
		elif check == 401:
			print("Unauthorized Client Error")
			sys.exit()
		elif check == 403:
			print("Forbidden URL Error")
			sys.exit()
		elif check == 404:
			print("URL Not found")
			sys.exit()
		elif check == 301:
			print("Site has been Permenantly Error")
			sys.exit()
		else: 
			print(check)
			print("Uncommon Error Code.")
			sys.exit()

		return check


	# Getting url with text and BS4 
	def get_proxies(self):

		text_url = requests.get(self.url).text
		response = requests.post(self.url, timeout=5)
		speed = response.elapsed.total_seconds() * 1000 
		print(speed)
		soup = BeautifulSoup(text_url, 'lxml')

		# Parsing DATA
		match = soup.find('section')
		d_match = match.find('div', class_="table-responsive")
		# Grabbing the tables themselves 
		table = d_match.table
		table_rows = table.find_all('tr')
		# Create two lists, one for IP Address, one for port numbers 
		ip_list = []
		port_list = []

		# Further Parsing data. In 'for loops' to grab table data inside of tables themselves
		# Finding the rows in the tables
		for row in table_rows:
			proxy = row.find_all('td')
			# Checking the type of proxy in comparision to the option set by the user 
			for i in proxy[4:5]:
				# If statment to check if they are the same
				if i.text == self.option:
					# If they are, iterate over the tables proxy IP's and append to a list 
					for i in proxy[:1]:
						ip_list.append(i.text)
					# iterate over the tables proxy port's and append to a list 
					for i in proxy[1:2]:
						port_list.append(i.text)
				else:
					pass
					

		# Combining the 2 lists
		# Making into a zipped tuple 

		zipped_proxy = zip(ip_list,port_list)

		# Converting to a list
		proxy_listed = list(zipped_proxy)

		# Joining the tuples together
		t_list = list(map(":".join, proxy_listed))

		return t_list

	def sort_proxies(self, plist):
		# Creating two lists for working proxies and their speeds
		workingProxies = []
		speedProxies = []
		url = "https://www.google.com"
		print("Testing Proxies abilities")
		print("-------------------------------------\n")
		numProxies = len(plist)
		print(f"Sorting {numProxies} {self.option} proxies")
		# Reading from the list itself 
		for i in plist:
			print(f"Testing Proxy {i}" )
			
			#If it gives us a good status code 
			try:
				gettit = requests.request('get',url, timeout=10, proxies={'https': i})
				workingProxies.append(i)
				print(Fore.WHITE)
				print(Style.BRIGHT, f"{i} was successful")
				print(Style.RESET_ALL)
			except:
				print(Fore.RED)
				print(Style.BRIGHT, f"{i} was unsuccessful")
				print(Style.RESET_ALL)

			
		# Checking the ability (speed) of working proxies 

		for i in workingProxies:
			print(f"Testing speed of proxy {i}")
			response = requests.post(url, timeout=5, proxies={'https': i})
			speed = response.elapsed.total_seconds() * 1000
			if speed < 150:
				print(Style.BRIGHT,f'{speed} milliseconds' )
				print(Style.RESET_ALL)
			elif speed > 200:
				print(Fore.RED,f'{speed} milliseconds' )
				print(Style.RESET_ALL)
			else:
				print(Fore.WHITE,f'{speed} milliseconds' )
				print(Style.RESET_ALL)

			
			
			# Appending to the list itself

			speedProxies.append(speed)

		#Working in the range of proxies and what they correspond to eachother
		print("\nCORRESPONDENCE")
		print("---------------------------------------------\n")
		for i in range(0, len(workingProxies)):
			print("{} corresponds to {}".format(workingProxies[i], speedProxies[i]))
			
		
		workingProxies, speedProxies = (list(t) for t in zip(*sorted(zip(speedProxies, workingProxies)))) #Sort the workingProxies based on their speed
		print(workingProxies)
		print(speedProxies)


				


			








