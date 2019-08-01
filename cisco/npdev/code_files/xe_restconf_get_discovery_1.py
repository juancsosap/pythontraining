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

    print("Make a request without headers, and so default to XML response.\n**")
    response = requests.get(url, verify=False, auth=auth)
    show_xml_response(response)

    print("Make a request with headers, and so get JSON response.\n**")
    headers = { 'Accept': 'application/vnd.yang.data+json' }
    response = requests.get(url, verify=False, headers=headers, auth=auth)
    show_json_response(response)

    print("Add the deep query parameter.\n**")
    response = requests.get(url+'?deep', verify=False, headers=headers, auth=auth)
    show_json_response(response)

def show_json_response(response):
    print("Status Code: " + str(response.status_code) + "\n")
    if response.text: 
        parse = json.loads(response.text) 
        print(json.dumps(parse, indent=4) + "\n")

def show_xml_response(response):
    print("Status Code: " + str(response.status_code) + "\n")
    if response.text: 
        print(response.text + "\n")
        
if __name__ == "__main__":
    main()
