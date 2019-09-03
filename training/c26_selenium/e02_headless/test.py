from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'http://automationpractice.com/index.php'

# Supported from Chrome version 60+
options = Options()  
options.add_argument("--headless")  

# Chrome must be installed
# https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome(executable_path=r'../drivers/chrome76-driver', options=options)
driver.get(url)

print(driver.title)
print(driver.current_url)

driver.close()