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
tag_url = base_url + "tag/"
verify = False
device_hostname = "csr1kv.cisco.com"

def main():

    device_id = get_hostname_id(device_hostname)
    print("Deleting tags associated with " + device_hostname + ".\n")
    for item in get_device_tags(device_id):
        print("Deleting tag " + get_tag(item['id']) + "\n")
        delete_tag(item['id'], device_id)

    tag = "Managed_by_ISP"
    print("Adding tag " + tag + ".\n")
    tag_id = add_tag(tag)
    print("The tag ID for the tag " + tag + " is " + tag_id + ".\n")

    print("Just to show how it can be done, given the tag name, get the tag ID.\n")
    print("The ID for tag " + tag + " is " + get_tag_id(tag) + ".\n")
    
    print("Associating tag " + tag + " with device with " + device_hostname + ".\n")
    tag_device(tag_id, device_id)

    print("The tags associated with " + device_hostname + " are:\n")
    for item in get_device_tags(device_id):
        print(get_tag(item['id']) + "\n")

    new_tag = "Managed_by_us"
    print("Changing name of tag " + tag + " to " + new_tag + ".\n")
    change_tag(tag_id, new_tag)

    print("The tags associated with " + device_hostname + " are:\n")
    for item in get_device_tags(device_id):
        print(get_tag(item['id']) + "\n")

def get_hostname_id(hostname):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    network_device_url = base_url + "network-device"
    result = requests.get(url=network_device_url+"?hostname="+hostname, headers=headers, verify=verify)
    for item in result.json()['response']:
        if item['hostname'] == hostname:
            return item['id']
    return None

def get_device_tags(device_id):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    result = requests.get(url=tag_url + "?resourceType=network-device&resourceId=" + device_id, headers=headers, verify=verify)
    return result.json()['response']

def delete_tag(tag_id, device_id):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    #Remove the association between the device and its location
    remove_url = tag_url + "association/" + tag_id + "?" + "resourceType=network-device&resourceId=" + device_id
    result = requests.delete(url=remove_url, headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for removing tag from device is: \n" + json.dumps(task_status, indent=2) + "\n")
    #Delete the location
    result = requests.delete(url=tag_url + tag_id, headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for deleting tag is: \n" + json.dumps(task_status, indent=2) + "\n")

def add_tag(tag):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    tag_payload = {'tag': tag }
    result = requests.post(url=tag_url, data=json.dumps(tag_payload), headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for adding tag is: \n" + json.dumps(task_status, indent=2) + "\n")
    return task_status['progress']

def get_tag_id(tag):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    result = requests.get(url=tag_url, headers=headers, verify=verify)
    for item in result.json()['response']:
        if item["tag"]==tag:
            return item['id']
    return None

def tag_device(tag_id, device_id):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    tag_payload = {'id': tag_id, 'resourceId': device_id, 'resourceType': 'network-device'}
    result = requests.post(url=tag_url + "/association", data=json.dumps(tag_payload), headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for adding tag is: \n" + json.dumps(task_status, indent=2) + "\n")

def get_tag(tag_id):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    result = requests.get(url=tag_url + tag_id, headers=headers, verify=verify)
    return result.json()['response']['tag']

def change_tag(tag_id, new_tag):
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}
    tag_payload = {'id': tag_id, 'tag': new_tag }
    result = requests.put(url=tag_url, data=json.dumps(tag_payload), headers=headers, verify=verify)
    task_status = check_task(result)
    print("Task status for adding tag is: \n" + json.dumps(task_status, indent=2) + "\n")
    return task_status['progress']

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

