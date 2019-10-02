from selenium import webdriver

import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'http://automationpractice.com/index.php'

# Mozilla Firefox must be installed
# https://github.com/mozilla/geckodriver/releases

# driver = webdriver.Firefox(executable_path=r'../drivers/firefox-driver')
# driver.get(url)
# driver.close()

# Chrome must be installed
# https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome(executable_path=r'../drivers/chrome76-driver')
driver.get(url)
driver.close()
