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
# Turn off warnings
requests.packages.urllib3.disable_warnings()
import time
import json

username = 'admin'
password = 'Cisco123!'
base_url = "https://apic-em:443/api/v1/"
verify = False

location_name = "SJC"
location_coords = "37.3639/-121.9289"
device_hostname = "csr1kv.cisco.com"

def main():
    
    device_id = get_hostname_id(device_hostname)
    print("The device id for the host " + device_hostname + " is " + device_id + ".\n")
    location_id = get_location_id(location_name)

    if location_id:
        print("The location id for the location " + location_name + " is " + location_id + ".\n")
        print("Deleting location so that it can be created again.\n")
        delete_location(location_id, device_id)
        
    location_id = add_location(location_name, location_coords)
    print("The location id for the new location " + location_name + " is " + location_id + ".\n")

    add_location_to_device(location_id, device_id)
    
    print("Show that the given device is at the given location by getting all devices for given location.\n") 
    show_devices_at_location(location_id)

def get_hostname_id(hostname):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    network_device_url = base_url + "network-device"
    result = requests.get(url=network_device_url+"?hostname="+hostname, headers=headers, verify=verify)
    for item in result.json()['response']:
        if item['hostname'] == hostname:
            return item['id']
    return None

def get_location_id(locationName):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    location_url = base_url + "location/location-name/" + locationName
    result = requests.get(url=location_url, headers=headers, verify=verify)
    return(result.json()['response']['id'])

def delete_location(location_id, device_id):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    #Remove the association between the device and its location
    network_device_url = base_url + "network-device/"
    result = requests.delete(url=network_device_url + device_id + "/location", headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for removing location from device is: \n" + json.dumps(task_status, indent=2) + "\n")
    #Delete the location
    location_url = base_url + "location/"
    result = requests.delete(url=location_url + location_id, headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for removing location is: \n" + json.dumps(task_status, indent=2) + "\n")

def add_location(locationName, geographicalAddress):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    location_url = base_url + "location/"
    location_payload = {'locationName': locationName, 'geographicalAddress': geographicalAddress }
    result = requests.post(url=location_url, data=json.dumps(location_payload), headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for adding location is: \n" + json.dumps(task_status, indent=2) + "\n")
    return task_status['progress']

def add_location_to_device(locationId, deviceId):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    net_device_location_url = base_url + "network-device/location"
    location_payload = {'id': deviceId, 'location': locationId}
    result = requests.post(url=net_device_location_url, data=json.dumps(location_payload), headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for adding location to device is: \n" + json.dumps(task_status, indent=2) + "\n")

def show_devices_at_location(location_id):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    result = requests.get(base_url + "network-device/location/" + location_id, headers=headers, verify=verify)
    print(json.dumps(result.json(), indent=2))
            
def get_token():
    ticket_url = base_url + 'ticket'
    payload = {'username': username, 'password': password}
    headers = {'content-type': "application/json"}
    response = requests.post(url=ticket_url, data=json.dumps(payload), headers=headers, verify=verify)
    token = response.json()['response']['serviceTicket']
    return token
    
def check_task(result):
    taskId = result.json()['response']['taskId']
    timeout = 15
    start = time.time()
    task_url = base_url + 'task/' + str(taskId)
    token = get_token()
    
    while True:
        while True:
            try:
                headers = {'x-auth-token': token,'content-type': "application/json"}
                result = requests.get(url=task_url, headers=headers, verify=verify)
                result.raise_for_status()
                break
            except requests.exceptions.HTTPError as e:
                print("Exception when checking task status - " + str(e) + "\n")
                if e.response.status_code == 401:
                    print("401 exception with request, refreshing token.\n")
                    token = get_token()

        response = result.json()['response']

        if 'endTime' in response:
            return response
        else:
            if start + timeout < time.time():
                raise TaskTimeoutError("Task %s did not complete within the specified timeout (%s seconds)" % (task_id, timeout))

            print("Task=%s has not completed yet. Sleeping %s seconds..." %(taskId, timeout/3) + "\n")
            time.sleep(timeout/3)

    return response
    
if __name__ == "__main__":
	main()
