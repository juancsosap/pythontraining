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
import collections
import random
requests.packages.urllib3.disable_warnings()

print("Start Q1.\n**")

base_url = 'https://apic/api/'

def main():
        
    # JSON credentials structure
    name_pwd = {'aaaUser': {'attributes': {'name': 'admin', 'pwd': 'cisco123'}}}
    
    # Log in to APIC
    print("Login\n**")
    response = requests.post(base_url + 'aaaLogin.json', data=json.dumps(name_pwd), verify=False)
    
    # Use cookies in response
    cookies = response.cookies
    print("Cookies are:\n")
    print(cookies)

    print("End Q1.\n**")

    print("Start Q2.\n**")

    # Define a tenant name for "Tenant_1"
    tn_name = "Tenant_1"

    # Get tenant
    print('Get ' + tn_name + '\n**')
    response = requests.get(create_tn_url(tn_name), cookies=cookies, verify=False)
    #Show result
    show_json_response(response)
        
    # The following block of code to delete the Tenant is for utility purposes as you are working through the code.
    # When the code is complete, this block will not be executed.
    # As you are completing the code, though, you will need this code to execute to ensure that the APIC database is clean.
    # If there is a Tenant, and you try to create another, there are circumstances under which you will see spurious errors.
    # To avoid spurious errors, delete the Tenant first. Note that the code block for Q8 also does this. 
    # If there is a tenant 
    if int(json.loads(response.text)['totalCount']) > 0:   
        #Make request to delete tenant
        print('Delete ' + tn_name + '\n**')
        response = requests.delete(create_tn_url(tn_name), cookies=cookies, verify=False)
        show_json_response(response)
        
    print("End Q2.\n**")
         
    print("Start Q3.\n**")

    # Make request to create Tenant
    print('Creating ' + tn_name + '\n**')
    tenant_data = create_tn_structure(tn_name)
    show_json_data(json.dumps(tenant_data))
    response = requests.post(create_tn_url(tn_name), data=json.dumps(tenant_data), cookies=cookies, verify=False)
    # Show result
    show_json_response(response)
    
    print("End Q3.\n**")
    
    print("Start Q4.\n**")
    
    # Create BD with the name "Web" for tenant
    BD_name = "Web"
    # Make request to create BD
    print('Creating ' + BD_name + '\n**')
    BD_data = create_BD_structure(tn_name, BD_name)
    show_json_data(json.dumps(BD_data))
    response = requests.post(create_BD_url(tn_name, BD_name), data=json.dumps(BD_data), cookies=cookies, verify=False)
    # Show result
    show_json_response(response)
    
    print("End Q4.\n**")
    
    print("Start Q5.\n**")
    
    # Create application with the name "MyApp" with an EPG of "Web" for tenant
    ap_name = "MyApp"
    epg_name = "Web"
    # Make request to create application
    print('Creating ' + ap_name + '\n**')
    ap_data = create_ap_structure(tn_name, ap_name, epg_name, BD_name)
    show_json_data(json.dumps(ap_data))
    response = requests.post(create_ap_url(tn_name, ap_name), data=json.dumps(ap_data), cookies=cookies, verify=False)
    # Show result
    show_json_response(response)
    
    print("End Q5.\n**")
    
    print("Start Q6.\n**") 
    
    # Get tenant with a query-target = subtree&rsp-prop-include=naming-only
    query_target = 'subtree&rsp-prop-include=naming-only'
    print('Get ' + tn_name + ' with query-target ' + query_target + '\n**')
    response = requests.get(create_tn_url(tn_name)+'?query-target='+query_target, cookies=cookies, verify=False)
    # Show result
    show_json_response(response)
    
    print("End Q6.\n**")
   
    print("Start Q7.\n**")
   
    # Get subnets class fvSubnet as XML
    print('Get subnets as XML.\n**')
    response = requests.get(base_url+'/class/fvSubnet.xml', cookies=cookies, verify=False)
    # Show result
    show_xml_response(response)
    
    print("End Q7.\n**")
   
    print("Start Q8.\n**")
   
    #Make request to delete Tenant
    print('Delete ' + tn_name + '\n**')
    response = requests.delete(create_tn_url(tn_name), cookies=cookies, verify=False)
    show_json_response(response)
    
    print("End Q8.\n**")

# Create a JSON URL to address a tenant given a name    
def create_tn_url(tn_name):
    return base_url + 'node/mo/uni/tn-' + tn_name + '.json'

# Create a JSON URL to address a BD for a tenant given a name    
def create_BD_url(tn_name, BD_name):
    return base_url + 'node/mo/uni/tn-' + tn_name + '/BD-' + BD_name + '.json'

# Create a JSON URL to address an application for a tenant given a name    
def create_ap_url(tn_name, ap_name):
    return base_url + 'node/mo/uni/tn-' + tn_name + '/ap-' + ap_name + '.json'
    
# Create a JSON tenant data structure given a name 
def create_tn_structure(tn_name):
    tn_structure = collections.OrderedDict() 
    tn_attributes = collections.OrderedDict()
 
    tn_attributes['dn'] = 'uni/tn-' + tn_name
    tn_attributes['name'] = tn_name
    tn_attributes['rn'] = 'tn-' + tn_name
    tn_attributes['status'] = 'created'
    
    tn_structure['fvTenant'] = {'attributes': tn_attributes,'children': [create_ctx_structure("Internal", tn_name)] }
    
    return tn_structure

# Create a JSON VRF context data structure given a context name and a tenant name 
def create_ctx_structure(ctx_name, tn_name):
    ctx_structure = collections.OrderedDict()
    ctx_atttributes = collections.OrderedDict()

    ctx_atttributes['dn'] = 'uni/tn-'+tn_name+'/ctx-' + ctx_name
    ctx_atttributes['name'] = ctx_name
    ctx_atttributes['rn'] = 'ctx-' + ctx_name
    ctx_atttributes['status'] = 'created'
    
    ctx_structure['fvCtx'] = {'attributes': ctx_atttributes,'children': [] }

    return ctx_structure

# Create a JSON VRF context relationship structure given a name 
def create_ctx_relation(ctx_name):
    ctx_relation = collections.OrderedDict()
    ctx_relation_atttributes = collections.OrderedDict()

    ctx_relation_atttributes['tnFvCtxName'] = ctx_name
    ctx_relation_atttributes['status'] = 'created,modified'
    
    ctx_relation['fvRsCtx'] = {'attributes': ctx_relation_atttributes,'children': [] }

    return ctx_relation

# Create a JSON BD data structure given a tenant name and a BD name 
def create_BD_structure(tn_name, BD_name):
    bd_structure = collections.OrderedDict()
    bd_attributes = collections.OrderedDict()

    bd_attributes['dn'] = 'uni/tn-' + tn_name + '/BD-' + BD_name
    bd_attributes['mac'] = generate_mac_address()
    bd_attributes['name'] = BD_name
    bd_attributes['rn'] = 'BD-' + BD_name
    bd_attributes['status'] = 'created'
    
    subnet = generate_subnet()

    bd_structure['fvBD'] = {'attributes': bd_attributes,
                  'children': [create_subnet_structure(tn_name, BD_name, subnet), create_ctx_relation("Internal")]}
    
    return bd_structure

# Create a JSON application data structure given a tenant name, application name, endpoint group name and BD name 
def create_ap_structure(tn_name, ap_name, epg_name, BD_name):
    ap_structure = collections.OrderedDict()
    ap_attributes = collections.OrderedDict()

    ap_attributes['dn'] = 'uni/tn-' + tn_name + '/ap-' + ap_name
    ap_attributes['name'] = ap_name
    ap_attributes['rn'] = 'ap-' + ap_name
    ap_attributes['status'] = 'created'
    
    ap_structure['fvAp'] = {'attributes': ap_attributes, 'children': [create_AEPg_structure(tn_name, ap_name, epg_name, BD_name)]}
    
    return ap_structure

# Create a JSON application endpoint group data structure  a tenant name, application name, endpoint group name and BD name 
def create_AEPg_structure(tn_name, ap_name, epg_name, BD_name):
    aepg_structure = collections.OrderedDict()
    aepg_attributes = collections.OrderedDict()

    aepg_attributes['dn'] = 'uni/tn-' + tn_name + '/ap-' + ap_name + '/epg-' + epg_name
    aepg_attributes['name'] = epg_name
    aepg_attributes['rn'] = 'epg-' + epg_name
    aepg_attributes['status'] = 'created'
    
    aepg_structure['fvAEPg'] = {'attributes': aepg_attributes, 'children': [create_BD_relation(BD_name)]}
    
    return aepg_structure

# Create a JSON BD relationship structure given a name 
def create_BD_relation(BD_name):
    bd_relation = collections.OrderedDict()
    bd_relation_attributes = collections.OrderedDict()

    bd_relation_attributes['tnFvBDName'] = BD_name
    bd_relation_attributes['status'] = 'created,modified'
    
    bd_relation['fvRsBd'] = {'attributes': bd_relation_attributes}
    
    return bd_relation

# Create a JSON subnet structure given a tenant name, BD name and subnet 
def create_subnet_structure(tn_name, BD_name, subnet):
    subnet_structure = collections.OrderedDict()
    subnet_attributes = collections.OrderedDict()

    subnet_attributes['dn'] = 'uni/tn-' + tn_name + '/BD-' + BD_name +'/subnet-[' + subnet + ']'
    subnet_attributes['ip'] = subnet
    subnet_attributes['rn'] = 'subnet-[' + subnet + ']'
    subnet_attributes['status'] = 'created'
    
    subnet_structure['fvSubnet'] = {'attributes': subnet_attributes, 'children': [] }
    
    return subnet_structure

# Create a dummy MAC address
def generate_mac_address():
    return '00:' + str(random.randint(10, 20)) + ':' + str(random.randint(10, 20)) + ':BD:F8:FF'

# Create a dummy subnet
def generate_subnet():
    return '10.1.' + str(random.randint(0, 256)) + '.1/24'

# Print a JSON response to the standard output
def show_json_response(response):
    print("Status Code: " + str(response.status_code) + "\n")
    if response.text: 
        show_json_data(response.text)

# Print a JSON data structure to standard output
def show_json_data(data):
    parse = json.loads(data) 
    print(json.dumps(parse, indent=4) + "\n")
    
# Print a XML response to the standard output
def show_xml_response(response):
    print("Status Code: " + str(response.status_code) + "\n") 
    print(response.text)
    
if __name__ == "__main__":
    main()
