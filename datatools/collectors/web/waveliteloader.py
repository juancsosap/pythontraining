from datatools.collectors.web.webwalker import *
import time

class WaveliteLoader(Navigator):
    def __init__(self, headless=True, wait=5, debug=False):
        super().__init__('wavelite', headless, wait, debug=debug)
        
    def actions(self, host):
        data = {}
        
        #LOGIN
        self.driver.find_element_by_id('u_name_box').send_keys('admin')
        self.driver.find_element_by_id('u_pass_box').send_keys('admin')
        self.driver.find_element_by_id('login_but').click()
        
        #CONFIG FRAME
        self.driver.switch_to.frame(self.driver.find_element_by_id('main_body'))
        self.driver.switch_to.frame(self.driver.find_element_by_id('config_sys'))
        
        #GENERAL TAB
        data['serialnumber'] = self.driver.find_element_by_id('SerialNumber').text
        data['partnumber'] = self.driver.find_element_by_id('PartNumber').text
        
        val = self.driver.find_element_by_xpath('//*[@id="gen_sys_info_table"]/tbody/tr[7]/td[2]').text
        xpath = '//*[@id="gen_sys_info_table"]/tbody/tr[8]/td[2]'
        data['uptime'] = val if 'hours' in val else self.driver.find_element_by_xpath(xpath).text
        
        data['temperature'] = self.driver.find_element_by_xpath('//*[@id="temperature"]/td[2]').text
        data['systemname'] = self.driver.find_element_by_name('sysName').get_attribute('value')
        systemname = data['systemname']
        
        #INVENTORY TAB
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id('tab_inventory').click()
        self.driver.switch_to.frame(self.driver.find_element_by_id('config_sys'))
        
        rows = self.driver.find_element_by_id('tbody').find_elements_by_tag_name('tr')
        items = {'systemname':[], 'itemname':[], 'description':[], 'serialnumber':[], 'partnumber':[], 'manufacturer':[]}
        for row in rows:
            cells = row.find_elements_by_tag_name('td')
            items['systemname'].append(systemname)
            items['itemname'].append(cells[0].text)
            items['description'].append(cells[1].text)
            items['serialnumber'].append(cells[2].text)
            items['partnumber'].append(cells[4].text)
            items['manufacturer'].append(cells[5].text)
            
        filepath = f'{self.folder}/{self.now}-items.csv'
        DataUtils.addtocsv(filepath, items)
        print(systemname, filepath)
        
        #IP TAB
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id('tab_ip').click()
        self.driver.switch_to.frame(self.driver.find_element_by_id('config_sys'))
        
        data['ip_address'] = self.driver.find_element_by_name('lanIpAddr').get_attribute('value')
        data['ip_netmask'] = self.driver.find_element_by_name('lanNetmask').get_attribute('value')
        
        filepath = f'{self.folder}/{self.now}-data.csv'
        DataUtils.addtocsv(filepath, data)
        print(systemname, filepath)
        
        #HWSTATUS HPANEL
        elements = ['PSU-1', 'PSU-2', 'FAN']
        hwstatus = {'systemname':[], 'element':[], 'present':[], 'partnumber':[], 'operstatus':[]}
        for element in elements:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('box_menu'))
            self.driver.switch_to.frame(self.driver.find_element_by_name('box_menu'))
            self.driver.find_element_by_id(element).click()
            present = self.driver.find_element_by_id(element).is_enabled()
            
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('main_body'))
            
            hwstatus['systemname'].append(systemname)
            hwstatus['element'].append(element)
            hwstatus['present'].append(present)
            hwstatus['partnumber'].append(self.driver.find_element_by_id('PartNumber').text if present else '')
            hwstatus['operstatus'].append(self.driver.find_element_by_id('OperStatus').text if present else '')
            
        filepath = f'{self.folder}/{self.now}-hwstatus.csv'
        DataUtils.addtocsv(filepath, hwstatus)
        print(systemname, filepath)
        
        #PORTS
        portstatus = {'systemname':[], 'element':[], 'porttype':[], 'portrate':[], 'adminstatus':[], 'operstatus':[], 'portalias':[]}
        for index in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20]:
            element = f'Port-{index}'
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('box_menu'))
            self.driver.switch_to.frame(self.driver.find_element_by_name('box_menu'))
            self.driver.find_element_by_id(element).click()
            
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('main_body'))
            self.driver.switch_to.frame(self.driver.find_element_by_id('config_port'))
            
            portstatus['systemname'].append(systemname)
            portstatus['element'].append(element)
            portstatus['porttype'].append(self.driver.find_element_by_id('PortType').text)
            portstatus['portrate'].append(self.driver.find_element_by_id('PortRate').text)
            portstatus['adminstatus'].append(self.driver.find_element_by_id('AdminStatus').text)
            portstatus['operstatus'].append(self.driver.find_element_by_id('OperStatus').text)
            portstatus['portalias'].append(self.driver.find_element_by_id('port_alias').get_attribute('value'))
            
        filepath = f'{self.folder}/{self.now}-portstatus.csv'
        DataUtils.addtocsv(filepath, portstatus)
        print(systemname, filepath)
        
        #FAULTS VTAB
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_id('main_menu'))
        self.driver.find_element_by_id('Fault').click()
        
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_id('box_menu'))
        self.driver.switch_to.frame(self.driver.find_element_by_name('box_menu'))
        self.driver.find_element_by_id('ALL').click()
        
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_id('main_body'))
        self.driver.switch_to.frame(self.driver.find_element_by_id('faults'))
        
        time.sleep(1)
        rows = self.driver.find_element_by_id('tbody').find_elements_by_tag_name('tr')
        alarms = {'systemname':[], 'time':[], 'source':[], 'severity':[], 'message':[], 'note':[]}
        for row in rows:
            cells = row.find_elements_by_tag_name('td')
            if len(cells) > 1:
                alarms['systemname'].append(systemname)
                alarms['time'].append(cells[0].text)
                alarms['source'].append(cells[1].text)
                alarms['severity'].append(cells[2].text)
                alarms['message'].append(cells[3].text)
                alarms['note'].append(cells[4].text)
            
        filepath = f'{self.folder}/{self.now}-alarms.csv'
        DataUtils.addtocsv(filepath, alarms)
        print(systemname, filepath)
        
        #PERFORMANCE VTAB
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_id('main_menu'))
        self.driver.find_element_by_id('Performance').click()
        
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_id('main_body'))
        
        rows = self.driver.find_element_by_id('tbody').find_elements_by_tag_name('tr')
        performance = {'systemname':[], 'port':[], 'vendor':[], 'type':[], 'wavelength':[], 'txpower':[], 'rxpower':[], 'temperature':[]}
        for row in rows:
            cells = row.find_elements_by_tag_name('td')
            if (len(cells) > 1) and (cells[4].text != ' '):
                performance['systemname'].append(systemname)
                performance['port'].append(cells[0].text)
                performance['vendor'].append(cells[1].text)
                performance['type'].append(cells[2].text)
                performance['wavelength'].append(cells[3].text)
                performance['txpower'].append(cells[4].text)
                performance['rxpower'].append(cells[5].text)
                performance['temperature'].append(cells[6].text)
            
        filepath = f'{self.folder}/{self.now}-performance.csv'
        DataUtils.addtocsv(filepath, performance)
        print(systemname, filepath)
        