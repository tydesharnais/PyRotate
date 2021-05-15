from src.proxygrab import Proxy
from dependencies import art
import os

# Cool colors
# Move to new script


def main():
	
	#Directory for Txt files
	directoryText = "/Users/tydesharnais/Desktop/project/dependencies/txt"
	importList = "/Users/tydesharnais/Desktop/project/dependencies/importList"


	print(art.header)
		#Simple menu

	print("Proxy Snatch by F_S/ash")
	print("------------------------\n")
	print("Simple Menu")
	print("1. Elite Proxy")
	print("2. Anonymous Proxy")
	print("3. Transparent Proxy")
	print("4. Import proxy list")
		
	loop = True
		# check conditions for proxy type
	while loop == True:
		ans = input("Enter Numerical Value: ")

		if ans == "1":
			print("")
				# Change the directory to the text files
			os.chdir(directoryText)
				# Open the tet file and read its lines 
			with open('elite.txt') as f:
				for line in f:
					print(line+ "\n")
			f.close()
			p_choice = input("Would you like to use this type of proxy?[Y/N]").upper()
			if p_choice == "Y":
				option = "elite proxy"
				print(option + " selected")
				loop = False
			else:
				print("Select another option")
				
		elif ans == "2":
			print("")
			os.chdir(directoryText)
			with open('anonymous.txt') as f:
				for line in f:
					print(line+ "\n")
			f.close()
			p_choice = input("Would you like to use this type of proxy?[Y/N]").upper()
			if p_choice == "Y":
				option = "anonymous"
				print(option + " selected")
				loop = False
			else:
				print("Select another option")

		elif ans == "3":
			print("")
			os.chdir(directoryText)
			with open('transparent.txt') as f:
				for line in f:
					print(line+ "\n")
			f.close()
			p_choice = input("Would you like to use this type of proxy?[Y/N]: ").upper()
			if p_choice == "Y" or "y":
				option = "transparent proxy"
				print(option + " selected")
				loop = False 
			else:
				print("Select another option")
		elif ans == "4":
			print("")
			os.chdir(importList)
			if os.path.exists('proxylist.txt'):
				print("Found proxy list")
				proxylist = []
				with open('proxylist.txt', "r") as filehandler:
					for line in filehandler:
						currentplace = line[:-1]
						proxylist.append(currentplace)
					print("Proxy List Uploaded.")
					iProxylist = Proxy("https://www.google.com", 3)
					iProxylist.sort_proxies(proxylist)

			else: 
				print("Could not find proxy list. Check your configuations and try again")
		else: 
			print("Sorry that option doesn't exist. Please reenter your choice.")
		
	url1 = "https://www.sslproxies.org"
	Proxy_1 = Proxy("https://www.sslproxies.org", option)
	listProxies = Proxy_1.get_proxies()
	print(listProxies)
	print(Proxy_1.sort_proxies(listProxies))

if __name__ == "__main__":
	main()

