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
discovery_url = base_url + 'discovery/'
discovery_name = 'discovery_challenge'
credential_url = base_url + 'global-credential/'
interface_url = base_url + 'interface/'
network_device_url = base_url + 'network-device/'

verify = False

def main():
    headers = {'x-auth-token': get_token(),'content-type': "application/json"}

    print("Start question 1 ******************************\n")

    print("Query for the discovery with the name " + discovery_name + " and delete it if it exists.\n")

    discovery_id = None
    try:
        #This is an undocumented API
        result = requests.get(url=discovery_url, headers=headers, verify=verify)
        result.raise_for_status()
        for item in result.json()['response']:
            if item['name'] == discovery_name:
                discovery_id = item['id'] 

        print("ID of discovery is " + str(discovery_id) + ".\n")
                
        if discovery_id:
            #See https://apic-em/swagger#!/discovery/deleteDiscoveryById (Inventory->discovery)
            result = requests.delete(url=discovery_url + discovery_id, headers=headers, verify=verify)
            result.raise_for_status()
            task_status = check_task(result)
            print("Task status when deleting discovery is: \n" + json.dumps(task_status, indent=2) + "\n")
    except requests.exceptions.HTTPError as e:
            print("Exception when deleting discovery - " + str(e) + "\n")

    print("End question 1 ******************************\n")

    print("Start question 2 ******************************\n")

    print("Get global credentials for credential subtypes CLI, SNMPV2_READ_COMMUNITY and SNMPV2_WRITE_COMMUNITY.\n")
    try:
        #See https://apic-em/swagger#!/device-credential/getGlobalCredential (Inventory->device-credential)
        result = requests.get(url=credential_url + "?credentialSubType=CLI", headers=headers, verify=verify)
        result.raise_for_status()
        for item in result.json()['response']:
            cli_credential_id = item['id']

        #See https://apic-em/swagger#!/device-credential/getGlobalCredentialSubTypeByID  (Inventory->device-credential)
        result = requests.get(url=credential_url + cli_credential_id, headers=headers, verify=verify)
        result.raise_for_status()
        print("CLI credentials subtype is " + json.dumps(result.json()['response']))
                    
        result = requests.get(url=credential_url + "?credentialSubType=SNMPV2_READ_COMMUNITY", headers=headers, verify=verify)
        result.raise_for_status()
        for item in result.json()['response']:
            snmpv2_read_credential_id = item['id']

        result = requests.get(url=credential_url + snmpv2_read_credential_id, headers=headers, verify=verify)
        result.raise_for_status()
        print("SNMP read credentials subtype is " + json.dumps(result.json()['response']))
            
        result = requests.get(url=credential_url + "?credentialSubType=SNMPV2_WRITE_COMMUNITY", headers=headers, verify=verify)
        result.raise_for_status()
        for item in result.json()['response']:
            snmpv2_write_credential_id = item['id']

        result = requests.get(url=credential_url + snmpv2_write_credential_id, headers=headers, verify=verify)
        result.raise_for_status()
        print("SNMP write credentials subtype is " + json.dumps(result.json()['response']))
    except requests.exceptions.HTTPError as e:
            print("Exception when getting global credentials - " + str(e) + "\n")
    
    print("End question 2 ******************************\n")

    print("Start question 3 ******************************\n")
    
    print("Create discovery with the name " + discovery_name + ", the IP address 192.168.1.11, and using global credentials.\n")

    discovery_payload = {
            "discoveryType":"Single",
            "ipAddressList":"192.168.1.11",
            "ipFilterList":[],
            "protocolOrder":"ssh",
            "cdpLevel":"16",
            "globalCredentialIdList":[cli_credential_id,snmpv2_read_credential_id,snmpv2_write_credential_id],
            "name": discovery_name
        }
    try:
        #See https://apic-em/swagger#!/discovery/insertDiscovery  (Inventory->discovery)
        result = requests.post(url=discovery_url, data=json.dumps(discovery_payload), headers=headers, verify=verify)
        result.raise_for_status()
        task_status = check_task(result)
        print("Task status when creating discovery is: \n" + json.dumps(task_status, indent=2) + "\n")
        discovery_id = task_status['progress']
    except requests.exceptions.HTTPError as e:
        print("Exception when creating discovery - " + str(e) + "\n")

    print("End question 3 ******************************\n")

    print("Start question 4 ******************************\n")

    print("Wait for discovery to complete.\n")

    discovery_complete = False
    while not discovery_complete:
        try:
            #See https://apic-em/swagger#!/discovery/getDiscoveryById  (Inventory->discovery)
            result = requests.get(url=discovery_url + discovery_id, headers=headers, verify=verify)
            result.raise_for_status()
            discoveryCondition = result.json()['response']['discoveryCondition']
            print("Discovery condition is " + discoveryCondition + ".\n")
            if discoveryCondition == 'Complete':
                discovery_complete = True
            else:
                print("Discovery not complete yet, sleeping 10 seconds.\n")
                time.sleep(10)
        except requests.exceptions.HTTPError as e:
            print("Exception when waiting for discovery to complete - " + str(e) + "\n")

    print("End question 4 ******************************\n")
    
    print("Start question 5 ******************************\n")

    print("Determine which devices were discovered.\n")
    try:
        #See https://apic-em/swagger#!/discovery/getNetworkDeviceByDiscoveryId (Inventory->discovery)
        result = requests.get(url=discovery_url + discovery_id + "/network-device", headers=headers, verify=verify)
        result.raise_for_status()
        for item in result.json()['response']:
            print(json.dumps(item, indent=2))
    except requests.exceptions.HTTPError as e:
        print("Exception when determining which devices were discovered - " + str(e) + "\n")

    print("End question 5 ******************************\n")

    print("Start question 6 ******************************\n")

    print("Determine which interfaces each reachable device has.\n")

    reachable_device_ids = []
    try:
        result = requests.get(url=discovery_url + discovery_id + "/network-device", headers=headers, verify=verify)
        result.raise_for_status()
        for item in result.json()['response']:
           if item['reachabilityStatus'] == "Success":
               reachable_device_ids.append(item['id'])
    except requests.exceptions.HTTPError as e:
        print("Exception when getting reachable devices - " + str(e) + "\n")

    print("Reachable device IDs are " + str(reachable_device_ids) + ".\n")

    try:
        for device_id in reachable_device_ids:
            #See https://apic-em/swagger#!/interface/getInterfaceByDeviceId (Inventory->interface)
            result = requests.get(url=interface_url + "network-device/" + device_id, headers=headers, verify=verify)
            result.raise_for_status()
            print("Interfaces for device with ID " + device_id + " are:\n")
            for item in result.json()['response']:
                print(json.dumps(item, indent=2))
    except requests.exceptions.HTTPError as e:
        print("Exception when determining which interfaces each reachable device has - " + str(e) + "\n")
        
    print("End question 6 ******************************\n")

    print("Start question 7 ******************************\n")

    print("Get the device configuration for reachable devices.\n")

    try:
        for device_id in reachable_device_ids:
            #See https://apic-em/swagger#!/network-device-config/getRunningConfig_0 (Inventory->network-device-config)
            result = requests.get(url=network_device_url + device_id + "/config", headers=headers, verify=verify)
            result.raise_for_status()
            print("Config for device with ID " + device_id + " is:\n")
            config_line = ''
            for item in result.json()['response']:
                config_line += item
                if item == "\n":
                    print(config_line)
                    config_line = ''
    except requests.exceptions.HTTPError as e:
        print("Exception when getting the device configuration for reachable devices - " + str(e) + "\n")
    
    print("End question 7 ******************************\n")
    
    
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
