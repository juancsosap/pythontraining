import unittest as ut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import time
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'http://automationpractice.com/index.php'

class PythonTest(ut.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()  
        options.add_argument("--headless")  
        driverstr = r'../drivers/chrome76-driver'
        cls.driver = webdriver.Chrome(executable_path=driverstr, options=options)

    def setUp(self):
        self.driver = self.__class__.driver
        self.driver.get(url)

    def test_home(self):
        # Assert
        self.assertEqual('My Store', self.driver.title)
    
    def test_search_success(self):
        # Arrange
        button = self.driver.find_element_by_class_name('button-search')

        # Act
        script = 'document.getElementsByName("search_query")[0].value = "Dress"'
        self.driver.execute_script(script)
        button.click()
        time.sleep(1)
        result = self.driver.page_source

        #Assert
        self.assertNotIn('No results were found for your search', result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    ut.main()
