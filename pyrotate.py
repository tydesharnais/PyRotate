import requests 
from bs4 import BeautifulSoup
import sys

# Set the Url vars
url = "https://www.sslproxies.org"
test_url = "https://www.google.com"
# Request the URL and print the status code
get_url = requests.get(url)
option = "transparent"
# Check conditional status code

if get_url.status_code == 200:
	print("Request status code 200")
elif get_url.status_code == 400:
	print("Bad Request Error")
	sys.exit()
elif get_url.status_code == 401:
	print("Unauthorized Client Error")
	sys.exit()
elif get_url.status_code == 403:
	print("Forbidden URL Error")
	sys.exit()
elif get_url.status_code == 404:
	print("URL Not found")
	sys.exit()
elif get_url.status_code == 301:
	print("Site has been Permenantly Error")
	sys.exit()
else: 
	print(get_url.status_code)
	print("Uncommon Error Code.")
	sys.exit()

# Getting url with text and BS4 

text_url = requests.get(url).text
response = requests.post(url, timeout=5)
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
		if i.text == option:
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

print("\n\n")
print(t_list)
#for length horseshit
#f_list_len = len(f_list)
#for i in range(0, f_list_len):

