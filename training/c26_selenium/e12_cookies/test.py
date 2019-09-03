import unittest as ut

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

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
        cls.driver.implicitly_wait(5)

    def setUp(self):
        self.driver = self.__class__.driver
        self.driver.get(url)

    def test_home(self):
        # Assert
        self.assertEqual('My Store', self.driver.title)
    
    def test_cookies(self):
        # Act
        all_cookies = self.driver.get_cookies()
        print(all_cookies)
        domain = all_cookies[0].get('domain', None)

        #Assert
        self.assertEqual('automationpractice.com', domain)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    ut.main()
