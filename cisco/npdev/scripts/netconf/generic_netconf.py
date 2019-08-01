from ncclient import manager
from lxml import etree

import json
import logging

def main():
  config_json = read_file('config.json')
  config = json.loads(config_json)

  if config['flags']['verbose']: set_logging()

  for host in config['hosts']:
    with manager.connect(host=host['name'], 
                         port=config['login']['port'], 
                         username=config['login']['user'], 
                         password=config['login']['pswd'],  
                         allow_agent=config['flags']['allow_agent'], 
                         look_for_keys=config['flags']['look_for_keys'], 
                         hostkey_verify=config['flags']['hostkey_verify']) as device:
    
      print("**Device {host}**\n".format(host = host['name']))

      datas = host.get('data', [])
      for script in config['scripts']:
        template = read_file(script['request'])
        data_id = script.get('data', -1)
        data = datas[data_id] if data_id > -1 else dict()
        
        request = template.format(**data)

        print("\n{desc}.\n**".format(desc=script['description']))
      
        if(script['config']):
          result = device.edit_config(target=script['target'], config=request, default_operation="merge")

          if script['target'] == 'candidate':
            device.commit()    
          
          result_str = str(result)
        else:
          result = device.get(('subtree', request))
          result_str = etree.tostring(result, pretty_print=True)

        if(config['flags']['console']):
          print (result_str)
        
        if(config['flags']['export']):
          write_file(script['result'], result_str)

def read_file(path):
    with open(path, 'r') as file:
      return file.read()

def write_file(path, content):
    with open(path, 'w') as file:
      file.write(content)

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