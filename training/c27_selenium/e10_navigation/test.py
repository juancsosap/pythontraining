import unittest as ut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

class PythonTest(ut.TestCase):

    @classmethod
    def setUpClass(cls):
        driverstr = r'../drivers/chrome76-driver'
        cls.driver = webdriver.Chrome(executable_path=driverstr)

    def setUp(self):
        self.driver = self.__class__.driver

    def test_navegation(self):
        # Arrange
        self.driver.get(r'http://python.org')

        time.sleep(3)

        self.driver.get(r'http://google.com')
        
        time.sleep(3)

        self.driver.get(r'http://youtube.com')
        
        # Act
        title0 = self.driver.title
        self.driver.back()
        
        time.sleep(3)

        title1 = self.driver.title
        self.driver.back()
        
        time.sleep(3)

        title2 = self.driver.title
        self.driver.forward()
        
        time.sleep(3)

        title3 = self.driver.title
        self.driver.forward()
        title4 = self.driver.title
        
        time.sleep(3)

        #Assert
        self.assertIn('YouTube', title0)
        self.assertIn('Google', title1)
        self.assertIn('Python', title2)
        self.assertIn('Google', title3)
        self.assertIn('YouTube', title4)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    ut.main()
