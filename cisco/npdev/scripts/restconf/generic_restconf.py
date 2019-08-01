import requests
import json
from jinja2 import Template
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

def main():
  config_json = read_file('config.json')
  config = json.loads(config_json)

  auth = HTTPBasicAuth(config['login']['user'], config['login']['pswd'])
  headers = {
    "Content-Type": "application/vnd.yang.data+xml",
    "Accept": "application/vnd.yang.data+xml"
  }

  for host in config['hosts']:

    datas = host.get('data', [])
    for script in config['scripts']:
      url = script['url'].format(host=host)
      
      if(script['method'] == 'post'):
        path = script['request']
        data_id = script.get('data', -1)
        data = datas[data_id] if data_id > -1 else dict()
        template = Template(path, **data)
        response = requests.post(url, data=template.render(), headers=headers, verify=False, auth=auth)
      
      if(script['method'] == 'get'):
        response = requests.get(url+'?deep', headers=headers, verify=False, auth=auth)
      
      show_xml_response(response)
      
def read_file(path):
    with open(path, 'r') as file:
      return file.read()

def write_file(path, content):
    with open(path, 'w') as file:
      file.write(content)

def show_xml_response(response):
    print("Status Code: " + str(response.status_code) + "\n")
    if response.text: 
        print(response.text + "\n")
        
if __name__ == "__main__":
    main()
