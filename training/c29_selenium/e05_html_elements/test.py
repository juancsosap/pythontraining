from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
    time.sleep(2)
    
    # Anchor
    login = driver.find_element_by_class_name('login')
    print('"', login.text, '" Link Clicked', sep='')
    login.click()

    print('-'*50)
    time.sleep(2)

    # Textbox
    email = driver.find_element_by_name('email_create')
    email.send_keys('mynewemail123@mail.com')
    print('"', email.get_attribute('id'), '" Textbox Filled', sep='')

    print('-'*50)
    time.sleep(2)

    # Button
    create = driver.find_element_by_id('SubmitCreate')
    print('"', create.text, '" Button Clicked', sep='')
    create.click()

    print('-'*50)
    time.sleep(2)

    # Radio Button
    divs = driver.find_elements(By.CLASS_NAME, 'radio-inline')
    for div in divs:
        label = div.find_element(By.TAG_NAME, 'label')
        input = label.find_element(By.TAG_NAME, 'input')
        text = label.text.strip()
        if('Mr.' == text): input.click()
        print(text, input.get_attribute('value'), input.is_selected(), sep=' : ')

    print('-'*50)
    time.sleep(2)
    
    # Textbox
    divs = driver.find_elements(By.CLASS_NAME, 'checkbox')
    for div in divs:
        label = div.find_element(By.TAG_NAME, 'label')
        input = div.find_element(By.TAG_NAME, 'input')
        text = label.text.strip()
        input.click()
        print(text, input.get_attribute('value'), input.is_selected(), sep=' : ')
    
    print('-'*50)
    time.sleep(2)

    # Select
    select = Select(driver.find_element(By.NAME, 'id_state'))
    for option in select.options:
        if(option.text == 'Oregon'): option.click()
        print(option.text, option.get_attribute('value'), option.is_selected(), sep=' : ')
    time.sleep(2)
    select.select_by_value('40')
    time.sleep(2)
    select.select_by_visible_text('Ohio')
    
    print('-'*50)
    time.sleep(2)
