# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python

import requests
import json
from jinja2 import Template
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

def main():

    auth = HTTPBasicAuth('cisco', 'cisco')
    url = 'http://csr1kv/restconf/api/config/native/interface'
    xml_headers = {'Content-Type': 'application/vnd.yang.data+xml'}


    gigabit_interface_data = Template(''' 
    <GigabitEthernet>
      <name>1</name>
      <ip>
        <address>
          <dhcp></dhcp>
        </address>
      </ip>
    </GigabitEthernet>
    ''')

    response = requests.post(url, data=gigabit_interface_data.render(), headers=xml_headers, verify=False, auth=auth)
    show_xml_response(response)
    
    print("Make a request without headers, and so default to XML response.\n**")
    response = requests.get(url+'?deep', verify=False, auth=auth)
    show_xml_response(response)

def show_xml_response(response):
    print("Status Code: " + str(response.status_code) + "\n")
    if response.text: 
        print(response.text + "\n")
        
if __name__ == "__main__":
    main()
