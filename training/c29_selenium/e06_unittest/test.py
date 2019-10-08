import unittest as ut

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import time
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'http://automationpractice.com/index.php'

class PythonTest(ut.TestCase):

    def setUp(self):
        options = Options()  
        #options.add_argument("--headless")  
        driverstr = r'../drivers/chrome76-driver'
        self.driver = webdriver.Chrome(executable_path=driverstr, options=options)
        self.driver.get(url)
        time.sleep(1)

    def test_search(self):
        # Arrange
        search = self.driver.find_element_by_name('search_query')
        button = self.driver.find_element_by_class_name('button-search')

        # Act
        search.send_keys('Dress')
        button.click()
        time.sleep(1)
        result1 = self.driver.page_source

        # Arrange
        search = self.driver.find_element_by_name('search_query')
        button = self.driver.find_element_by_class_name('button-search')

        # Act
        search.send_keys('Computer')
        button.click()
        time.sleep(1)
        result2 = self.driver.page_source

        #Assert
        self.assertNotIn('No results were found for your search', result1)
        self.assertIn('No results were found for your search', result2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    ut.main()
