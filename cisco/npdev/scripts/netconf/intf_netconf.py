from ncclient import manager
from lxml import etree

import json
import logging

def main():
  config_json = read_file('config_intf.json')
  config = json.loads(config_json)

  if config['flags']['verbose']: set_logging()

  for host in config.hosts:
    with manager.connect(host=host['fqdn'], 
                         port=config['login']['port'], 
                         username=config['login']['user'], 
                         password=config['login']['pswd'],  
                         allow_agent=config['flags']['allow_agent'], 
                         look_for_keys=config['flags']['look_for_keys'], 
                         hostkey_verify=config['flags']['hostkey_verify']) as device:
    
      frequest = read_file('requests/{sw}/{sw}_request_filter_intf.xml'.format(sw=host['sw']))
      arequest = read_file('requests/{sw}/{sw}_request_add_intf.xml'.format(sw=host['sw']))
      drequest = read_file('requests/{sw}/{sw}_request_delete_intf.xml'.format(sw=host['sw']))
    
      print("**Device {fqdn}**\n".format(fqdn=host['fqdn']))

      print("\nShow which interfaces exist. There should only be one GigabitEthernet interface.\n**")
      result = device.get(('subtree', frequest))
      print (etree.tostring(result.data_ele, pretty_print=True))

      print("\nAdd a Loopback interface.\n**")
      result = device.edit_config(target=config['login']['target'], config=arequest, default_operation="merge")
      print (result)
      if config['login']['target'] == 'candidate':
        device.commit()

      print("\nShow that the Loopback interface has been added.\n**")
      result = device.get(('subtree', frequest))
      print (etree.tostring(result.data_ele, pretty_print=True))

      print("\nDelete the Loopback interface.\n**")
      result = device.edit_config(target=config['login']['target'], config=drequest, default_operation="merge")
      print (result)
      if config['login']['target'] == 'candidate':
        device.commit()
        
      print("\nShow that the Loopback interface has been deleted.\n**")
      result = device.get(('subtree', frequest))
      print (etree.tostring(result.data_ele, pretty_print=True))
    
def read_file(path):
    with open(path, 'r') as file:
      return file.read()

def set_logging():
  LOGGING_TO_ENABLE = [
    'ncclient.transport.ssh',
    'ncclient.transport.session',
    'ncclient.operations.rpc'
  ]

  handler = logging.StreamHandler()
  for l in LOGGING_TO_ENABLE:
    logger = logging.getLogger(l)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    main()