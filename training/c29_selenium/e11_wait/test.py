import unittest as ut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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

    def setUp(self):
        self.driver = self.__class__.driver
        self.driver.get(url)

    def test_home(self):
        # Assert
        self.assertEqual('My Store', self.driver.title)
    
    def test_search_success(self):
        # Arrange
        # Explicit Wait
        # It wait only one element
        condition = ec.presence_of_element_located((By.NAME, 'search_query'))
        search = WebDriverWait(self.driver, 10).until(condition)
        # Implicit Wait
        # It is used to wait any follow DOM requested element if it is not available yet
        self.driver.implicitly_wait(10) # Default value 0
        button = self.driver.find_element_by_name('submit_search')

        # Act
        search.send_keys('Dress')
        button.click()
        result = self.driver.page_source

        #Assert
        self.assertNotIn('No results were found for your search', result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    ut.main()
