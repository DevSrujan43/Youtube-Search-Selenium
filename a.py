from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Accessing youtube 
driver.get("https://www.youtube.com/")

# for searching the search bar 
search = driver.find_element_by_id("search") 
# inputing the song we wish to hear 
search.send_keys("One direction Night Changes")
search.send_keys(Keys.RETURN)

# Delay for 5 seconds
time.sleep(5)

# Closes the automated browser
driver.close()
