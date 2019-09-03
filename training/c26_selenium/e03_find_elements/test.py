from selenium import webdriver

import time 
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'http://automationpractice.com/index.php'

# Chrome must be installed
# https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome(executable_path=r'../drivers/chrome76-driver')
driver.get(url)

print(driver.title)

search = driver.find_element_by_name('search_query')
search.send_keys('Dress')

time.sleep(1)

button = driver.find_element_by_class_name('button-search')
button.click()

time.sleep(1)


xpath = '//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a'
item = driver.find_element_by_xpath(xpath)
item.click()

time.sleep(1)

description = driver.find_element_by_tag_name('h1')
print(description.text)

driver.close()
