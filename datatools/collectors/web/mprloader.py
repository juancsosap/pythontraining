from datatools.collectors.web.webwalker import *
import time

class MPRLoader(Navigator):
    def __init__(self, headless=True, wait=5, debug=False, ftype='date'):
        super().__init__('mpr', headless, wait, debug=debug, ftype=ftype)
        
    def actions(self, host):
        #LOGIN
        self.driver.find_element_by_id('username').send_keys('initial')
        self.driver.find_element_by_id('userpassword').send_keys('adminadmin')
        self.driver.find_element_by_name('in-log-ib-signin').click()
        self.driver.find_element_by_name('in-cob-ib-accept').click()
        hostname = self.driver.title
        print(host, '-', hostname)

        #SEARCH
        self.driver.find_element_by_name('in-gen-hl-mm').click()
        dashboard = self.driver.find_element_by_name('mm-rda-bu-dir').find_element_by_xpath('..')
        items = dashboard.find_element_by_xpath('..').find_elements_by_tag_name('li')
        odus = [item.find_element_by_tag_name('a').get_attribute('name') for item in items]
        links = [item.find_element_by_tag_name('a').get_attribute('href') for item in items]
        print('ODUS:', odus)

        #DOWNLOAD
        for odu, link in zip(odus, links):
            self.driver.get(link)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ExportBtn')))
            try:
                self.wait.until(EC.text_to_be_present_in_element_value((By.NAME, 'mm-rda-ct-Ch1RxElTime24'), '--'))
                time.sleep(1)
                print(f'ERROR: {odu}')
            except: pass
            self.driver.find_element_by_class_name('ExportBtn').click()

        #MOVE FILES
        savefolder = f'{self.folder}'
        print('Stored:', savefolder)
        