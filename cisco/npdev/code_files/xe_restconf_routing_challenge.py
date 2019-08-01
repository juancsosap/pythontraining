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
import time
import collections
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()


def main():

    print("Start Q1.\n**")

##    auth = HTTPBasicAuth(<REPLACE for Q1>, <REPLACE for Q1>)
      ##Set headers for JSON formatted data
##    headers = { 
##        'Accept': 'application/vnd.yang.data+<REPLACE for Q1>', 
##        'Content-Type': 'application/vnd.yang.data+<REPLACE for Q1>' 
##    } 

      ##This command will help:
      ##pyang -p ~/git/yang --tree-path native/ip/route -f tree ned.yang | more
##    route_url = "http://csr1kv/restconf/api/config/native/<REPLACE for Q1>"
##    routes_to_add = create_routes_to_add()
##    empty_route_table = {"ned:route": {}}

##    print("Get IP routes with all parameters\n**") 
##    response = requests.<REPLACE for Q1>(route_url+<REPLACE for Q1>, verify=False, headers=headers, auth=auth) 
##    show_json_response(response) 

    print("End Q1.\n**")

    print("Start Q2.\n**")
        
##    print("Add routes - " + str(routes_to_add) + "\n**") 
##    response = requests.<REPLACE for Q2>(route_url, data=json.dumps(routes_to_add), verify=False, headers=headers, auth=auth) 
##    show_json_response(response) 

    print("End Q2.\n**")

    print("Start Q3.\n**")

##    print("Get IP routes and expect to see additional routes added\n**") 
##    response = requests.<REPLACE for Q3>(route_url+<REPLACE for Q3>", verify=False, headers=headers, auth=auth) 
##    show_json_response(response) 

    print("End Q3.\n**")

    print("Start Q4.\n**")

##    print("Delete the \"50.40.40.0,255.255.255.0\" route.\n**")
##    response = requests.<REPLACE for Q4>(route_url+"/<REPLACE for Q4>/50.40.40.0,255.255.255.0", verify=False, headers=headers, auth=auth)
##    show_json_response(response) 

##    print("Get IP routes and expect NOT to see \"50.40.40.0,255.255.255.0\" route.\n**") 
##    response = requests.<REPLACE for Q4>(route_url+<REPLACE for Q4>, verify=False, headers=headers, auth=auth) 
##    show_json_response(response) 

    print("End Q4.\n**")

    print("Start Q5.\n**")
    
##    print("Delete all routes.\n**")
##    response = requests.<REPLACE for Q5>(<REPLACE for Q5>, verify=False, headers=headers, auth=auth) 
##    show_json_response(response) 

##    print("Get IP routes and expect NOT to see any routes.\n**") 
##    response = requests.<REPLACE for Q5>(route_url+<REPLACE for Q5>, verify=False, headers=headers, auth=auth) 
##    show_json_response(response)

    print("End Q5.\n**")
    
def show_json_response(response):
    print("Status Code: " + str(response.status_code) + "\n")
    if response.text: 
        parse = json.loads(response.text) 
        print(json.dumps(parse, indent=4) + "\n")

def create_routes_to_add():
    route = collections.OrderedDict() 

    route['prefix'] = '50.40.40.0' 
    route['mask'] = '255.255.255.0' 
    route['fwd-list'] = [{'fwd': '192.168.1.1'}]
    ip_route_list = [route.copy()]

    route['prefix'] = '0.0.0.0' 
    route['mask'] = '0.0.0.0' 
    route['fwd-list'] = [{'fwd': '192.168.1.1'}]
    ip_route_list.append(route.copy())

    route['prefix'] = '10.0.0.0' 
    route['mask'] = '255.0.0.0' 
    route['fwd-list'] = [{'fwd': '192.168.1.1'}]
    ip_route_list.append(route.copy())

    route['prefix'] = '20.20.20.0' 
    route['mask'] = '255.255.255.0' 
    route['fwd-list'] = [{'fwd': '192.168.1.1'}]
    ip_route_list.append(route.copy())

    route['prefix'] = '30.30.30.0' 
    route['mask'] = '255.255.255.0' 
    route['fwd-list'] = [{'fwd': '192.168.1.1'}]
    ip_route_list.append(route.copy())

    route['prefix'] = '172.16.0.0' 
    route['mask'] = '255.255.0.0' 
    route['fwd-list'] = [{'fwd': '192.168.1.1'}]
    ip_route_list.append(route.copy())
    
    routes_to_add = { 
        "ned:route": { 
            "ip-route-interface-forwarding-list": ip_route_list 
        } 
    }

    return routes_to_add
        
if __name__ == "__main__":
    main()
