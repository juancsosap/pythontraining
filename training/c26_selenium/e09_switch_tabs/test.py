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

    def test_tabs(self):
        # Arrange
        script = 'window.open("")'
        self.driver.execute_script(script)
        handle = self.driver.window_handles[1]
        
        time.sleep(3)

        # Act
        self.driver.get(r'http://python.org')
        title0 = self.driver.title
        self.driver.switch_to.window(handle)

        time.sleep(3)

        self.driver.get(r'http://google.com')
        title1 = self.driver.title
        
        time.sleep(3)

        self.driver.execute_script(script)
        handle = self.driver.window_handles[2]
        self.driver.switch_to.window(handle)
        self.driver.get(r'http://youtube.com')
        title2 = self.driver.title
        
        time.sleep(3)

        #Assert
        self.assertIn('Python', title0)
        self.assertIn('Google', title1)
        self.assertIn('YouTube', title2)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close() # Close only one tab

        time.sleep(3)

        cls.driver.quit() # Close all the windows



if __name__ == "__main__":
    ut.main()
