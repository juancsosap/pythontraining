import unittest as ut

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = 'http://automationpractice.com/index.php'

class PythonTest(ut.TestCase):

    @classmethod
    def setUpClass(cls):
        driverstr = r'../drivers/chrome76-driver'
        cls.driver = webdriver.Chrome(executable_path=driverstr)
        cls.driver.implicitly_wait(5)

    def setUp(self):
        self.driver = self.__class__.driver
        self.driver.get(url)

    def test_home(self):
        # Assert
        self.assertEqual('My Store', self.driver.title)

    def test_mouse(self):
        # Arrange
        search = self.driver.find_element(By.NAME, 'search_query')
        button = self.driver.find_element(By.NAME, 'submit_search')
        mouse = ActionChains(self.driver)
        
        # Act
        search.send_keys('Dress')
        mouse.move_to_element(button).click().perform()
        
        time.sleep(1)

        #Assert
        self.assertIn('results have been found', self.driver.page_source)
        self.assertNotIn('No results were found for your search', self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    ut.main()
