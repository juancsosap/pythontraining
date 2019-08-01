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
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

def main():

    auth = HTTPBasicAuth('cisco', 'cisco')
    url = 'http://csr1kv/restconf/api/config/native/interface'
    xml_headers = {'Content-Type': 'application/vnd.yang.data+xml'}

    loopback_interface_data_min = """ 
    <Loopback>
      <name>1</name>
    </Loopback>
    """

    loopback_interface_data_primary_address = """ 
    <Loopback>
      <name>1</name>
      <ip>
        <address>
          <primary>
            <address>10.101.1.2</address>
            <mask>255.255.255.0</mask>
          </primary>
        </address>
      </ip>
    </Loopback>
    """

    loopback_interface_data_secondary_address = """ 
    <Loopback>
      <name>1</name>
      <ip>
        <address>
          <secondary>
            <address>10.101.1.3</address>
            <mask>255.255.255.0</mask>
          </secondary>
        </address>
      </ip>
    </Loopback>
    """

    print("Add a new interface.\n**"+loopback_interface_data_min)
    response = requests.put(url+"/Loopback/1", data=loopback_interface_data_min, headers=xml_headers, verify=False, auth=auth)
    print("See response code 201, indicating created.\n**")
    show_xml_response(response)

    print("Get interfaces and expect to see both the GigabitEthernet and Loopback interfaces.\n**")
    response = requests.get(url, verify=False, auth=auth)
    show_xml_response(response)
        
    print("Patch the Loopback interface to add primary address.\n**"+loopback_interface_data_primary_address)
    response = requests.patch(url+"/Loopback", data=loopback_interface_data_primary_address, headers=xml_headers, verify=False, auth=auth)
    print("See response code 204, indicating no body in reponse, but success.\n**")
    show_xml_response(response)

    print("Get the Loopback interface addresses and expect to see Loopback interface primary address.\n**")
    response = requests.get(url+"/Loopback/1/ip/address", verify=False, auth=auth)
    show_xml_response(response)
    
    print("Attempt to put the Loopback interface to add secondary address.\n**"+loopback_interface_data_secondary_address)
    response = requests.put(url+"/Loopback/1", data=loopback_interface_data_secondary_address, headers=xml_headers, verify=False, auth=auth)
    print("See response code 400, and error message \"primary/mask is not configured\".\n**")
    show_xml_response(response)

    print("Patch the Loopback interface to add secondary address.\n**"+loopback_interface_data_secondary_address)
    response = requests.patch(url+"/Loopback", data=loopback_interface_data_secondary_address, headers=xml_headers, verify=False, auth=auth)
    print("See response code 204, indicating no body in reponse, but success.\n**")
    show_xml_response(response)

    print("Get the Loopback interface addresses and expect to see Loopback interface primary and secondary addresses.\n**")
    response = requests.get(url+"/Loopback/1/ip/address", verify=False, auth=auth)
    show_xml_response(response)
    
    print("Delete the Loopback/1 interface resource.\n**")
    response = requests.delete(url+'/Loopback/1', verify=False, auth=auth)
    print("See response code 204, indicating no content returned.\n**")
    show_xml_response(response)

    print("\nGet interfaces and expect to see only the GigabitEthernet interface.\n**")
    response = requests.get(url, verify=False, auth=auth)
    show_xml_response(response)
    
def show_xml_response(response):
    print("Status Code: " + str(response.status_code) + "\n")
    if response.text: 
        print(response.text + "\n")
   
if __name__ == "__main__":
    main()
