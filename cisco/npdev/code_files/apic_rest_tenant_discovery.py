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

import json
import requests
import time
requests.packages.urllib3.disable_warnings()

username = 'admin'
password = 'cisco123'
base_url = "https://apic.cisco.com/api/"
#Do not use cookies directly, use get_cookies() to make sure that the cookies are refreshed.
cookies = {}
verify = False
tenant_1_url = base_url + 'node/mo/uni/tn-Tenant_1.json'
epg_application_url = base_url + "node/mo/uni/tn-Tenant_1/ap-MyApp/epg-Application.json"

nodes_data = {
    'TEP-1-101': {
        'nodeId': '201',
        'name': 'leaf201'
        },
    'TEP-1-103': {
            'nodeId': '101',
            'name': 'spine101'
        },
    'TEP-1-102': {
        'nodeId': '202',
        'name': 'leaf202'
        }
    }

def main():

    try :
        #Discovering the fabric will take a few minutes if the fabric has not been discovered already.
        discover_fabric()
            
        delete_tenant_1()
    
        create_tenant_1()    
    
        # Get Tenant_1 with all subclasses
        print("Get Tenant_1.************************************************************\n")
        result = requests.get(url=tenant_1_url+"?query-target=subtree", cookies=get_cookies(), verify=verify)
        result.raise_for_status()       
        # Show result
        show_json_result(result)
   
        print("Get Tenant_1 with selected subclasses.************************************************************\n")
        result = requests.get(url=tenant_1_url+"?query-target=subtree&target-subtree-class=fvAEPg,fvAp,fvSubnet,fvBD,fvCtx,fvTenant", 
                            cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
    
        add_contract()

        print("Get Tenant_1 contract subclasses.************************************************************\n")
        result = requests.get(url=tenant_1_url+"?query-target=subtree&target-subtree-class=vzBrCP", cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)

        add_static_path()
 
        print("Get Application EPG paths.************************************************************\n")
        result = requests.get(url=epg_application_url+"?query-target=subtree&target-subtree-class=fvRsPathAtt", cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
        
        print("Waiting for the dust to settle before analyzing health...\n")
        time.sleep(30)
        print("Analyzing MyApp health.************************************************************\n")
        analyze_health()
   
        #Make request to delete Tenant_1. This can be uncommented for debug purposes
        #print("Delete Tenant_1\n**")
        #result = requests.post(tenant_1_url, data=tenant_1_delete, cookies=cookies, verify=verify)
        #show_json_result(result)
    except Exception as e:
        print("Exception - " + str(e) + "\n")

#Always use this method to get the cookies so that the session is refreshed.
#Do not use the global variable cookies, except in this method to refresh the session.
def get_cookies():
    global cookies
    credentials = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
    
    try:
        if 'APIC-Cookie' in cookies:
            print("Refresh session.\n")
            result = requests.post(base_url + 'aaaRefresh.json', data=json.dumps(credentials), cookies=cookies, verify=verify)
            #show_json_result(result)
            result.raise_for_status()
        else:
            print("Login.\n")
            result = requests.post(base_url + 'aaaLogin.json', data=json.dumps(credentials), verify=verify)
            #show_json_result(result)
            result.raise_for_status()
  
        # Get token from login result structure
        auth_token = json.loads(result.text)['imdata'][0]['aaaLogin']['attributes']['token']
    
        # Create cookie from token
        cookies['APIC-Cookie'] = auth_token
   
    except Exception as e:
        print("Exception when managing session - " + str(e) + "\n")
        cookies = {}
        raise
    
    return cookies
    
def discover_fabric():

    try:
        while True:
            node_identities = get_node_identities()
            for item in node_identities['imdata']:
                if item['dhcpClient']['attributes']['clientEvent'] == 'denied':
                    serial = item['dhcpClient']['attributes']['id']
                    update_node(serial, nodes_data[serial]['name'], nodes_data[serial]['nodeId'])
            if node_identities['totalCount'] == '3':
                break
            print("Wait 30 seconds for node to become fully configured and/or additional nodes to be discovered.\n")
            time.sleep(30)
    except Exception as e:
        print("Exception when discovering fabric - " + str(e) + "\n")
        
def get_node_identities():
    
    print("Getting node identities.\n")

    node_identities_url = base_url + ("""node/class/topology/pod-1/node-1/dhcpClient.json""" +
    """?query-target-filter=or(eq(dhcpClient.nodeRole,"leaf")""" +
    """,eq(dhcpClient.nodeRole,"spine")""" +
    """,eq(dhcpClient.nodeRole,"unsupported"))""")

    try:
        result = requests.get(url=node_identities_url, cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
        return result.json()
    except requests.exceptions.HTTPError as e:
        print("Exception when getting node identities - " + str(e) + "\n")
        raise

def update_node(serial, name, nodeId):
    
    print("Updating node with serial " + serial + ", name " + name + " and id " + nodeId + ".\n")
    
    update_node = {'fabricNodeIdentP':{
        'attributes':{
            'dn':'uni/controller/nodeidentpol/nodep-' + serial,
            'serial':serial,
            'nodeId':nodeId,
            'name':name,
            'status':'created,modified'},
        'children':[]}}
        
    node_update_url = base_url + "node/mo/uni/controller/nodeidentpol.json"
    try:
        result = requests.post(url=node_update_url, data=json.dumps(update_node), cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
    except requests.exceptions.HTTPError as e:
        print("Exception when updating node - " + str(e) + "\n")
        raise

def delete_tenant_1():
    # JSON structure to delete Tenant_1
    tenant_1_delete = """{"fvTenant":{
        "attributes":{
            "dn":"uni/tn-Tenant_1",
            "name":"Tenant_1",
            "rn":"tn-Tenant_1",
            "status":"deleted"},
            "children":[]}
        }"""
   
    try:
        print("Get Tenant_1\n**")
        result = requests.get(url=tenant_1_url, cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
            
        if int(result.json()['totalCount']) > 0:   
            print("Delete Tenant_1\n**")
            result = requests.post(url=tenant_1_url, data=tenant_1_delete, cookies=cookies, verify=verify)
            result.raise_for_status()
            show_json_result(result)
    except Exception as e:
        print("Exception when deleting tenant - " + str(e) + "\n")
        raise

def create_tenant_1():
    tenant_1_create = """{"fvTenant":{
    "attributes":{
        "dn":"uni/tn-Tenant_1",
        "name":"Tenant_1",
        "rn":"tn-Tenant_1",
        "status":"created"},
        "children":[{
            "fvCtx":{
                "attributes":{
                    "dn":"uni/tn-Tenant_1/ctx-Internal",
                    "name":"Internal",
                    "rn":"ctx-Internal",
                    "status":"created"},
                    "children":[]
                    }
        },
        {"fvBD":{
            "attributes":{
                "dn":"uni/tn-Tenant_1/BD-Web",
                "mac":"00:22:BD:F8:19:FF",
                "name":"Web",
                "rn":"BD-Web",
                "status":"created"},
                "children":[{
                    "fvSubnet":{
                        "attributes":{
                            "dn":"uni/tn-Tenant_1/BD-Web/subnet-[10.1.1.1/24]",
                            "ip":"10.1.1.1/24",
                            "rn":"subnet-[10.1.1.1/24]",
                            "status":"created"},
                            "children":[]}
                },
                {"fvRsCtx":{
                    "attributes":{
                        "tnFvCtxName":"Internal",
                        "status":"created,modified"},
                        "children":[]}
                }
                ]
        }
        },
        {"fvBD":{
            "attributes":{
                "dn":"uni/tn-Tenant_1/BD-Application",
                "mac":"00:22:BD:F8:19:FE",
                "name":"Application",
                "rn":"BD-Application",
                "status":"created"},
                "children":[{
                    "fvSubnet":{
                        "attributes":{
                            "dn":"uni/tn-Tenant_1/BD-Application/subnet-[10.1.2.1/24]",
                            "ip":"10.1.2.1/24",
                            "rn":"subnet-[10.1.2.1/24]",
                            "status":"created"},
                            "children":[]}
                },
                {"fvRsCtx":{
                    "attributes":{
                        "tnFvCtxName":"Internal",
                        "status":"created,modified"},
                        "children":[]}
                }
                ]
        }
        },
        {"fvBD":{
            "attributes":{
                "dn":"uni/tn-Tenant_1/BD-Database",
                "mac":"00:22:BD:F8:19:FD",
                "name":"Database",
                "rn":"BD-Database",
                "status":"created"},
                "children":[{
                    "fvSubnet":{
                        "attributes":{
                            "dn":"uni/tn-Tenant_1/BD-Database/subnet-[10.1.3.1/24]",
                            "ip":"10.1.3.1/24",
                            "rn":"subnet-[10.1.3.1/24]",
                            "status":"created"},
                            "children":[]}
                },
                {"fvRsCtx":{
                    "attributes":{
                        "tnFvCtxName":"Internal",
                        "status":"created,modified"},
                        "children":[]}
                }
                ]
        }
        },
        {"fvAp":{
            "attributes":{
                "dn":"uni/tn-Tenant_1/ap-MyApp",
                "name":"MyApp",
                "rn":"ap-MyApp",
                "status":"created"},
                "children":[{
                    "fvAEPg":{"attributes":{
                        "dn":"uni/tn-Tenant_1/ap-MyApp/epg-Web",
                        "name":"Web",
                        "rn":"epg-Web",
                        "status":"created"},
                        "children":[{
                            "fvRsBd":{
                                "attributes":{
                                    "tnFvBDName":"Web",
                                    "status":"created,modified"},
                                    "children":[]
                                    }
                        }]
                        }
                },
                {
                    "fvAEPg":{"attributes":{
                        "dn":"uni/tn-Tenant_1/ap-MyApp/epg-Application",
                        "name":"Application",
                        "rn":"epg-Application",
                        "status":"created"},
                        "children":[{
                            "fvRsBd":{
                                "attributes":{
                                    "tnFvBDName":"Application",
                                    "status":"created,modified"},
                                    "children":[]
                                    }
                        }]
                        }
                },
                {
                    "fvAEPg":{"attributes":{
                        "dn":"uni/tn-Tenant_1/ap-MyApp/epg-Database",
                        "name":"Database",
                        "rn":"epg-Database",
                        "status":"created"},
                        "children":[{
                            "fvRsBd":{
                                "attributes":{
                                    "tnFvBDName":"Database",
                                    "status":"created,modified"},
                                    "children":[]
                                    }
                        }]
                        }
                }]
                }
        } 
        }
    }"""
    
    try:
        print("Creating Tenant_1\n**")
        result = requests.post(url=tenant_1_url, data=tenant_1_create, cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
    except Exception as e:
        print("Exception when creating tenant - " + str(e) + "\n")
        raise
    
def add_contract():
    application_database_all_contract = """{
        "fvTenant": {
            "attributes": {
                "dn": "uni/tn-Tenant_1",
                "status": "modified"
            },
            "children": [
                {
                    "fvAp": {
                        "attributes": {
                            "dn": "uni/tn-Tenant_1/ap-MyApp",
                            "status": "modified"
                        },
                        "children": [
                            {
                                "fvAEPg": {
                                    "attributes": {
                                        "dn": "uni/tn-Tenant_1/ap-MyApp/epg-Application",
                                        "status": "modified"
                                    },
                                    "children": [
                                        {
                                            "fvRsCons": {
                                                "attributes": {
                                                    "tnVzBrCPName": "Application_Database_All",
                                                    "status": "created,modified"
                                                },
                                                "children": [
                                                ]
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "fvAEPg": {
                                    "attributes": {
                                        "dn": "uni/tn-Tenant_1/ap-MyApp/epg-Database",
                                        "status": "modified"
                                    },
                                    "children": [
                                        {
                                            "fvRsProv": {
                                                "attributes": {
                                                    "tnVzBrCPName": "Application_Database_All",
                                                    "status": "created,modified"
                                                },
                                                "children": [
                                                ]
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                },
                {
                    "vzBrCP": {
                        "attributes": {
                            "dn": "uni/tn-Tenant_1/brc-Application_Database_All",
                            "name": "Application_Database_All",
                            "scope": "tenant",
                            "status": "created"
                        },
                        "children": [
                            {
                                "vzSubj": {
                                    "attributes": {
                                        "dn": "uni/tn-Tenant_1/brc-Application_Database_All/subj-Subject",
                                        "name": "Subject",
                                        "status": "created"
                                    },
                                    "children": [
                                        {
                                            "vzRsSubjFiltAtt": {
                                                "attributes": {
                                                    "tnVzFilterName": "default",
                                                    "status": "created,modified"
                                                },
                                                "children": [
                                                ]
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }"""

    try:
        print("Adding Application_Database_All contract for Tenant_1\n**")
        result = requests.post(url=tenant_1_url, data=application_database_all_contract, cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
    except Exception as e:
        print("Exception when adding contract - " + str(e) + "\n")
        raise

def add_static_path():
    print("Add static path to Application EPG\n**")    
    path_structure = """
    {"fvRsPathAtt":{"attributes":{"encap":"vlan-1","tDn":"topology/pod-1/paths-201/pathep-[eth1/1]","status":"created"},"children":[]}}"""

    try:
        result = requests.post(url=epg_application_url, data=path_structure, cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
    except Exception as e:
        print("Exception when adding static path - " + str(e) + "\n")
        raise
        
def analyze_health():

    try:
        my_app_health_url = base_url + "node/mo/uni/tn-Tenant_1/ap-MyApp.json?query-target=children&rsp-subtree-include=health,fault-count"
    
        result = requests.get(url=my_app_health_url, cookies=get_cookies(), verify=verify)
        result.raise_for_status()
        show_json_result(result)
        
        for app_item in result.json()['imdata']:
            app_name = app_item['fvAEPg']['attributes']['name']
            app_children = app_item['fvAEPg']['children']
            for app_child in app_children:
                if 'healthNodeInst' in app_child.keys():
                    if int(app_child.get('healthNodeInst')['attributes']['cur']) < 100:
                        print("Health of " + app_name + " less than 100, drilling in.\n")
                        app_health_url = base_url + "node/mo/uni/tn-Tenant_1/ap-MyApp/epg-" + app_name + ".json?query-target=self&rsp-subtree-include=health"
                        result = requests.get(url=app_health_url, cookies=get_cookies(), verify=verify)
                        result.raise_for_status()
                        show_json_result(result)
                        
                        for node_item in result.json()['imdata']:
                            node_children = node_item['fvAEPg']['children']
                            for node_child in node_children:
                                if 'healthNodeInst' in node_child.keys():
                                    if int(app_child.get('healthNodeInst')['attributes']['cur']) < 100:
                                        nodeId = app_child.get('healthNodeInst')['attributes']['nodeId']
                                        node_health_url = base_url + ("node/mo/topology/pod-1/node-" + nodeId + 
                                                                      "/local/svc-policyelem-id-0/uni/epp/fv-[uni/tn-Tenant_1/ap-MyApp/epg-" + app_name + 
                                                                      "]/node-" + nodeId + ".json?query-target=children&rsp-subtree-include=health,fault-count")
                                        result = requests.get(url=node_health_url, cookies=get_cookies(), verify=verify)
                                        result.raise_for_status()
                                        show_json_result(result)
                                        
                                        for path_item in result.json()['imdata']:
                                            if 'fvStPathAtt' in path_item.keys():
                                                pathName = path_item.get('fvStPathAtt')['attributes']['pathName']
                                                path_children = path_item['fvStPathAtt']['children']
                                                for path_child in path_children:
                                                    if 'healthInst' in path_child.keys():
                                                        if int(path_child.get('healthInst')['attributes']['cur']) < 100:
                                                            path_faults_url = base_url + ("node/mo/topology/pod-1/node-" + nodeId + "/sys/phys-[" + pathName + 
                                                                                          "].json?rsp-subtree-include=faults,no-scoped,subtree&order-by=faultInfo.severity|desc&page=0&page-size=15")
                                                            result = requests.get(url=path_faults_url, cookies=get_cookies(), verify=verify)
                                                            result.raise_for_status()
                                                            show_json_result(result)       
        
    except Exception as e:
        print("Exception when analyzing health - " + str(e) + "\n")
        raise

def show_json_result(result):
    print("Status Code: " + str(result.status_code) + "\n")
    if result.text: 
        parse = json.loads(result.text) 
        print(json.dumps(parse, indent=2) + "\n")
        
if __name__ == "__main__":
    main()
