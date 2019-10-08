from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  

import time 
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'http://automationpractice.com/index.php'

# Chrome must be installed
# https://sites.google.com/a/chromium.org/chromedriver/downloads
with webdriver.Chrome(executable_path=r'../drivers/chrome76-driver') as driver:
    driver.get(url)

    print('-'*50)

    print(driver.title)

    print('-'*50)

    unorder_list = driver.find_element_by_id('homefeatured')
    items = unorder_list.find_elements_by_tag_name('li')
    for item in items:
        link = item.find_element_by_class_name('product-name')
        info_block = item.find_element_by_class_name('right-block') 
        price = info_block.find_element_by_class_name('price')
        text_disc = ''
        try:
            span_disc = info_block.find_element_by_class_name('price-percent-reduction')
            text_disc = '(' + span_disc.text + ')'
        except: pass
        print(price.text, link.text, text_disc)
