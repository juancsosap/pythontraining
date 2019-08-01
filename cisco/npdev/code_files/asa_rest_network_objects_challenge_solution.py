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

    print("Start Q1.\n**")

    print("Use the Token Service to get a token and construct request headers with that token.\n**")

    token_url = "https://asa/api/tokenservices" 
    auth = HTTPBasicAuth('cisco', 'cisco')
    headers = {'Content-Type': 'application/json'}

    response = requests.post(token_url, headers=headers, auth=auth, verify=False)
    token = response.headers['x-auth-token']

    headers = {'Content-Type': 'application/json',
               'x-auth-token': token}
        
    print("Show the headers and expect a non null \"x-auth-token\" value.\n**")
    print(headers)
    
    print("End Q1.\n**")

    print("Start Q2.\n**")

    networkobjects_url = "https://asa/api/objects/networkobjects"
    
    print("Get all network objects and expect to see no items.\n**")
    response = requests.get(networkobjects_url, headers=headers, verify=False)
    show_json_response(response)

    print("End Q2.\n**")

    print("Start Q3.\n**")

    print("Create file_server_1 network object.\n**")

    file_server_1_payload = {
        "host": { 
            "kind": "IPv4Address", 
            "value": "203.0.113.10" 
        }, 
        "kind": "object#NetworkObj", 
        "name": "file_server_1", 
        "objectId": "file_server_1" 
    }

    response = requests.post(networkobjects_url, data=json.dumps(file_server_1_payload), headers=headers, verify=False)
    show_json_response(response)

    print("Get file_server_1 network object.\n**")
    response = requests.get(networkobjects_url+"/file_server_1", headers=headers, verify=False)
    show_json_response(response)

    print("End Q3.\n**")

    print("Start Q4.\n**")
    
    print("Try to create file_server_1 network object again and expect an error.\n**")
    response = requests.post(networkobjects_url, data=json.dumps(file_server_1_payload), headers=headers, verify=False)
    show_json_response(response)

    print("End Q4.\n**")

    print("Start Q5.\n**")
    
    print("Change file_server_1 IPv4Address address to \"203.0.113.20\".\n**")
    
    network_object_patch = {
    "host": {
        "kind": "IPv4Address",
        "value": "203.0.113.20"
        }
    }

    response = requests.patch(networkobjects_url+"/file_server_1", data=json.dumps(network_object_patch), headers=headers, verify=False)
    show_json_response(response)

    print("Get file_server_1 network object and expect to see the new address.\n**")
    response = requests.get(networkobjects_url+"/file_server_1", headers=headers, verify=False)
    show_json_response(response)

    print("End Q5.\n**")

    print("Start Q6.\n**")
    
    print("Change the name of the \"file_server_1\" network object at \"203.0.113.20\" to \"file_server_2\".\n**")
    file_server_2_put = {
        "host": {
            "kind": "IPv4Address", 
            "value": "203.0.113.20"
        }, 
        "kind": "object#NetworkObj", 
        "objectId": "file_server_1", 
        "name": "file_server_2"
    }

    response = requests.put(networkobjects_url+"/file_server_1", data=json.dumps(file_server_2_put), headers=headers, verify=False)
    show_json_response(response)

    print("Get the \"file_server_2\" network object.\n**")
    response = requests.get(networkobjects_url+"/file_server_2", headers=headers, verify=False)
    show_json_response(response)

    print("End Q6.\n**")

    print("Start Q7.\n**")
    
    print("Delete file_server_2 network object.\n**")
    response = requests.delete(networkobjects_url+"/file_server_2", headers=headers, verify=False)
    show_json_response(response)

    print("Get all network objects and expect to see no items.\n**")
    response = requests.get(networkobjects_url, headers=headers, verify=False)
    show_json_response(response)

    print("End Q7.\n**")

    print("Start Q8.\n**")
        
    print("Bulk create web_server_1 and file_server_3 network objects.\n**")

    # See https://asa/doc/#feature/bulk
    bulk_url = "https://asa/api"
    
    file_server_3_payload = {
        "host": { 
            "kind": "IPv4Address", 
            "value": "203.0.113.30" 
        }, 
        "kind": "object#NetworkObj", 
        "name": "file_server_3", 
        "objectId": "file_server_3" 
    } 
    
    web_server_1_payload = {
        "host": { 
            "kind": "IPv4Address", 
            "value": "203.0.113.40" 
        }, 
        "kind": "object#NetworkObj", 
        "name": "web_server_1", 
        "objectId": "web_server_1" 
    }
        
    bulk_post_payload = [
        {
            "method": "POST",
            "resourceUri": "/api/objects/networkobjects",
            "data": file_server_3_payload
        },
        {
            "method": "POST",
            "resourceUri": "/api/objects/networkobjects",
            "data": web_server_1_payload
        }
    ]
     
    response = requests.post(bulk_url, data=json.dumps(bulk_post_payload), headers=headers, verify=False)
    show_json_response(response)

    print("Get all network objects and expect to see \"web_server_1\" and \"file_server_3\".\n**")
    response = requests.get(networkobjects_url, headers=headers, verify=False)
    show_json_response(response)

    print("End Q8.\n**")

    print("Start Q9.\n**")
    
    print("Bulk delete file_server_3 and web_server_1 network objects.\n**")
    
    bulk_delete_payload = [
        {
            "method": "DELETE",
            "resourceUri": "/api/objects/networkobjects/file_server_3"
        },
        {
            "method": "DELETE",
            "resourceUri": "/api/objects/networkobjects/web_server_1"
        }
    ]
        
    response = requests.post(bulk_url, data=json.dumps(bulk_delete_payload), headers=headers, verify=False)
    show_json_response(response)

    print("Get all network objects and expect to see no items.\n**")
    response = requests.get(networkobjects_url, headers=headers, verify=False)
    show_json_response(response)

    print("End Q9.\n**")
    
def show_json_response(response):
    print("Status Code: " + str(response.status_code) + "\n")
    if response.text: 
        parse = json.loads(response.text) 
        print(json.dumps(parse, indent=4) + "\n")

if __name__ == "__main__":
    main()

    

