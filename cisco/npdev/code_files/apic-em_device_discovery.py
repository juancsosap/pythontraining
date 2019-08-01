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

def main():
    token = get_token()

    print("Code block 1 ******************************")
    print("Try the request and expect to fail, as the URL is invalid. So expect an exception with a 403 status code.\n")
    discovery_payload = {'id': 58, 'discoveryStatus': 'Active'}
    try:
        headers = {'x-auth-token': token, 'content-type': "application/json"}
        result = requests.put(url=base_url, data=json.dumps(discovery_payload), headers=headers, verify=verify)
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Exception when setting discovery status - " + str(e) + "\n")
    
    #This is a deliberately invalid token to illustrate service ticket exception handling.
    token = ''

    discovery_url = base_url + 'discovery'

    print("Code block 2 ******************************")
    print("Try the request and initially fail with an exception with a 401 status code, as the token is invalid.")
    print("The exception handling will refresh the token.\n")
    while True: 
        try:
            headers = {'x-auth-token': token, 'content-type': "application/json"}
            result = requests.put(url=discovery_url, data=json.dumps(discovery_payload), headers=headers, verify=verify)
            result.raise_for_status()
            if result.status_code != 202:
                print("Response code is not 202, so no task was created.\n")
            else:
                taskId = result.json()['response']['taskId']
                task_status = check_task(taskId)
                print("Task status is: \n" + json.dumps(task_status, indent=2) + "\n")
            break
        except requests.exceptions.HTTPError as e:
            print("Exception when setting discovery status - " + str(e) + "\n")
            if e.response.status_code == 401:
                print("401 exception with request, refreshing token.\n")
                token = get_token()

    print("Code block 3 ******************************")
    print("Try the request and succeed, but the body is invalid, so the task status will have an error message.\n")
    discovery_payload = {'id': 1, 'discoveryStatus': 'Active'}
    while True: 
        try:
            headers = {'x-auth-token': token, 'content-type': "application/json"}
            result = requests.put(url=discovery_url, data=json.dumps(discovery_payload), headers=headers, verify=verify)
            result.raise_for_status()
            if result.status_code != 202:
                print("Response code is not 202, so no task was created.\n")
            else:
                taskId = result.json()['response']['taskId']
                task_status = check_task(taskId)
                print("Task status is: \n" + json.dumps(task_status, indent=2) + "\n")
            break
        except requests.exceptions.HTTPError as e:
            print("Exception when setting discovery status - " + str(e) + "\n")
            if e.response.status_code == 401:
                print("401 exception with request, refreshing token.\n")
                token = get_token()

    print("Code block 4 ******************************")
    print("Try a put request with an invalid URL for a PUT.")
    print("The server will not know what to do, so expect an exception with a 500 status code.\n")
    while True: 
        try:
            headers = {'x-auth-token': token, 'content-type': "application/json"}
            result = requests.put(url=discovery_url+"/58", headers=headers, verify=verify)
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Exception when setting discovery status - " + str(e) + "\n")
            if e.response.status_code == 401:
                print("401 exception with request, refreshing token.\n")
                token = get_token()
            if e.response.status_code == 500:
                print("500 exception with request, server has no idea what is going on.\n")
                break

    print("Code block 5 ******************************")
    print("Try a get request with an invalid ID. The resource does not exist, so expect an exception with a 404 status code.\n")
    while True: 
        try:
            headers = {'x-auth-token': token, 'content-type': "application/json"}
            result = requests.get(url=discovery_url+"/1", headers=headers, verify=verify)
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Exception when setting discovery status - " + str(e) + "\n")
            if e.response.status_code == 401:
                print("401 exception with request, refreshing token.\n")
                token = get_token()
            if e.response.status_code == 404:
                print("404 exception with request, ID incorrect.\n")
                break

    print("Code block 6 ******************************")
    print("Try a delete request with an invalid ID. The task status will show the error.\n")
    while True: 
        try:
            headers = {'x-auth-token': token, 'content-type': "application/json"}
            result = requests.delete(url=discovery_url+"/1", headers=headers, verify=verify)
            result.raise_for_status()
            if result.status_code != 202:
                print("Response code is not 202, so no task was created.\n")
            else:
                taskId = result.json()['response']['taskId']
                task_status = check_task(taskId)
                print("Task status is: \n" + json.dumps(task_status, indent=2) + "\n")
            break
        except requests.exceptions.HTTPError as e:
            print("Exception when setting discovery status - " + str(e) + "\n")
            if e.response.status_code == 401:
                print("401 exception with request, refreshing token.\n")
                token = get_token()
          
def get_token():
    ticket_url = base_url + 'ticket'
    payload = {'username': username, 'password': password}
    headers = {'content-type': "application/json"}
    response = requests.post(url=ticket_url, data=json.dumps(payload), headers=headers, verify=verify)
    token = response.json()['response']['serviceTicket']
    return token
    
def check_task(taskId):
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
