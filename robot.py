from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from fake_useragent import UserAgent

#PROXY var
PROXY = "168.181.62.74:36928"
#Set options
options = Options()
options.add_argument("window-size=1400,600")
options.add_argument('--proxy-server=%s' % PROXY)

#The User agent 
ua = UserAgent()
a = ua.random
user_agent = ua.random
print(user_agent)
options.add_argument(f'user-agent={user_agent}')
chrome_path = "/Users/tydesharnais/Desktop/project/chromedriver"
driver = webdriver.Chrome(chrome_path,options=options)
driver.get('https://whoer.net//')
#driver.get("https://www.youtube.com/watch?v=6xYlcKxRVrc")


sleep(30)
driver.quit()