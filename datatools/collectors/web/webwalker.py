from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from datatools.utils import *

class Navigator:
    dirpath = 'datatools/collectors/web/configs'
    
    def __init__(self, category, headless=True, wait=5, debug=False, ftype='date'):
        self.config = FileUtils.readjson(f'{Navigator.dirpath}/{category}.json')
        self.debug = debug
        
        options = Options()
        options.headless = headless

        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        profile.set_preference("browser.download.manager.closeWhenDone", False)
        profile.set_preference("browser.download.manager.focusWhenStarting", False)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", self.config['mimetypes'])

        self.now = dt.datetime.now()
        subfolder = dt.date.today() if ftype == 'date' else self.now
        self.folder = f"{self.config['savefolder']}/{subfolder}"
        FileUtils.mkfolder(self.folder)
        profile.set_preference("browser.download.dir", self.folder)
        
        self.driver = webdriver.Firefox(options=options, firefox_profile=profile)
        self.driver.implicitly_wait(wait)

        self.mouse = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, wait)
    
    def actions(self):
        pass
    
    def load(self):
        for host in self.config['hosts']:
            url = f"{self.config['protocol']}://{host}/"
            if self.debug:
                self.driver.get(url)
                self.actions(host)
            else:
                try:
                    self.driver.get(url)
                    self.actions(host)
                except Exception as e:
                    print(host, '- ERROR:', e)
                    if self.debug: self.driver.get_screenshot_as_file(f"error-{host}.png")
            print()
        return str(dt.date.today())
