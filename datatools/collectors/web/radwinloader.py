from datatools.collectors.web.webwalker import *
import time

class RadwinLoader(Navigator):
    def __init__(self, headless=True, wait=5, debug=False):
        super().__init__('radwin', headless, wait, debug=debug)
        
    def actions(self, host):
        data = {}
        
        #LOGIN
        self.driver.find_element_by_name('UserName').send_keys('admin')
        self.driver.find_element_by_name('Password').send_keys('admin')
        self.driver.find_element_by_class_name('Login').find_element_by_xpath('..').click()
        
        #MONITOR
        data['link_state'] = self.driver.find_element_by_id('LinkState').text.replace('\n', '')
        data['sector_id'] = self.driver.find_element_by_id('SectorID').text.replace('\n', '')
        data['hsu_location'] = self.driver.find_element_by_id('HsuLocation').text.replace('\n', '')
        data['hbs_location'] = self.driver.find_element_by_id('HbsLocation').text.replace('\n', '')
        data['frecuency'] = self.driver.find_element_by_id('Frequency').text.replace('\n', '')
        data['hsu_ip'] = self.driver.find_element_by_id('HsuIP').text.replace('\n', '')
        data['hbs_ip'] = self.driver.find_element_by_id('HbsIP').text.replace('\n', '')
        data['band'] = self.driver.find_element_by_id('Band').text.replace('\n', '')
        data['hsu_rss'] = self.driver.find_element_by_id('HsuRss').text.replace('\n', '')
        data['hbs_rss'] = self.driver.find_element_by_id('HbsRss').text.replace('\n', '')
        data['channel_bw'] = self.driver.find_element_by_id('CBW').text.replace('\n', '')
        data['hsutxrxrate'] = self.driver.find_element_by_id('HsuTxRxRate').text.replace('\n', '')
        data['hbstxrxrate'] = self.driver.find_element_by_id('HbsTxRxRate').text.replace('\n', '')
        data['hsu_state'] = self.driver.find_element_by_id('HsuState').text.replace('\n', '')
        data['hsu_throughput'] = self.driver.find_element_by_id('HsuTput').text.replace('\n', '')
        data['hbs_throughput'] = self.driver.find_element_by_id('HbsTput').text.replace('\n', '')
        data['gps_latitude'] = self.driver.find_element_by_id('GpsLatitude').text.replace('\n', '')
        data['gps_longitude'] = self.driver.find_element_by_id('GpsLongitude').text.replace('\n', '').replace('""', '"')
        data['gps_altitude'] = self.driver.find_element_by_id('GpsAltitude').text.replace('\n', '').replace('""', '"')
        
        #CONFIG
        self.driver.find_element_by_id('localA').click()
        data['site_name'] = self.driver.find_element_by_id('SiteName').get_attribute('value')
        data['up_time'] = self.driver.find_element_by_id('upTime').text.replace('\n', '')
        
        self.driver.find_element_by_xpath('//*[@id="System"]/div[2]/ul/li[3]/a').click()
        fields = ['product', 'hw_version', 'sw_version', 'mac_address', 'serial_number', 'agg_capacity']
        for index, field in enumerate(fields):
            xpath = f'//*[@id="Inventory"]/div[4]/div[1]/table/tbody/tr[{index+1}]/td[2]'
            data[field] = self.driver.find_element_by_xpath(xpath).text.replace('\n', '')
        
        data['datetime'] = self.now
        sitename = data['site_name']
        filepath = f'{self.folder}/data.csv'
        DataUtils.addtocsv(filepath, data)
        print(sitename, filepath)
        
        self.driver.find_element_by_class_name('BackBtn').click()
        
        #EVENTS
        self.driver.find_element_by_id('RecentEvents').click()
        time.sleep(1)
        
        rows = self.driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        events = {'site_name':[], 'severity':[], 'time':[], 'description':[], 'interface':[]}
        for row in rows:
            cells = row.find_elements_by_tag_name('td')
            events['site_name'].append(sitename)
            events['severity'].append(cells[1].text.replace('\n', ''))
            events['time'].append(cells[2].text.replace('\n', ''))
            events['description'].append(cells[3].text.replace('\n', ''))
            events['interface'].append(cells[4].text.replace('\n', ''))
        self.driver.find_element_by_class_name('BackBtn').click()
        
        filepath = f'{self.folder}/events.csv'
        DataUtils.addtocsv(filepath, events)
        print(sitename, filepath)
        