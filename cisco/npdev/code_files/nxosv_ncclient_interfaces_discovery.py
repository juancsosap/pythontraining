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

from ncclient import manager

def main():

    with manager.connect(host='nxosv', port=22, username='cisco', password='cisco',
                         hostkey_verify=False, device_params={'name': 'nexus'},
                         allow_agent=False, look_for_keys=False) as nxosv:
              
        #Use CLI commands to change the interface description, and back again.
        current_description = get_interface_value(nxosv, 'desc')
        print('Current description is ' + current_description)

        interface_description_commands = ['configure terminal', 'interface Ethernet2/6', 'description Configured by Python ncclient']
        nc_config_reply = nxosv.exec_command(interface_description_commands)
        print(nc_config_reply)

        new_description = get_interface_value(nxosv, 'desc')
        print('New description is ' + new_description)
        
        interface_description_commands = ['config t', 'int e2/6', 'desc ' + current_description]
        nc_config_reply = nxosv.exec_command(interface_description_commands)
        print(nc_config_reply)

        current_description = get_interface_value(nxosv, 'desc')
        print('Changed back description is ' + current_description)

        #Use CLI commands to change the interface speed, and back again.
        current_speed = get_interface_value(nxosv, 'eth_speed')
        print('Current speed is ' + current_speed)
      
        interface_speed_commands = ['configure terminal', 'interface Ethernet2/6', 'speed 100']
        nc_config_reply = nxosv.exec_command(interface_speed_commands)
        print(nc_config_reply)
    
        new_speed = get_interface_value(nxosv, 'eth_speed')
        print('New speed is ' + new_speed)

        #The value that the configuration return for an interface with auto-speed setting can't be used to
        #configure it. To configure auto speed, you need to use the CLI equivalent of 'speed auto'.
        if current_speed == 'auto-speed':
            current_speed = 'auto'
            
        interface_speed_commands = ['configure terminal', 'interface Ethernet2/6', 'speed ' + current_speed]
        nc_config_reply = nxosv.exec_command(interface_speed_commands)
        print(nc_config_reply)
        
        current_speed = get_interface_value(nxosv, 'eth_speed')
        print('Changed back speed is ' + current_speed)

        #Use CLI commands to change the interface state, and back again.
        current_state = get_interface_value(nxosv, 'admin_state')
        print('Current state is ' + current_state)

        if current_state == 'down':
            interface_state_commands = ['configure terminal', 'interface Ethernet2/6', 'no shut']
        else:
            interface_state_commands = ['configure terminal', 'interface Ethernet2/6', 'shut']

        nc_config_reply = nxosv.exec_command(interface_state_commands)
        print(nc_config_reply)

        new_state = get_interface_value(nxosv, 'admin_state')
        print('New state is ' + new_state)

        if new_state == 'down':
            interface_state_commands = ['configure terminal', 'interface Ethernet2/6', 'no shut']
        else:
            interface_state_commands = ['configure terminal', 'interface Ethernet2/6', 'shut']
        
        nc_config_reply = nxosv.exec_command(interface_state_commands)
        print(nc_config_reply)
        
        current_state = get_interface_value(nxosv, 'admin_state')
        print('Changed back state is ' + current_state)
                
#Use a subtree filter to get a specific interface and parse out the named value.
def get_interface_value(nxosv, element_name):
    show_interface_filter = """<show><interface><value>Ethernet2/6</value></interface></show>"""
    nc_get_reply = nxosv.get(('subtree', show_interface_filter))
    nc_get_reply_no_ns = remove_namespaces(nc_get_reply.data_ele)
    element_value = nc_get_reply_no_ns.find('.//' + element_name)
    if str(element_value) == "None":
        return "None"
    else:
        return(nc_get_reply_no_ns.find('.//' + element_name).text)

#The namespaces in the XML response make life awkward, so this function cleanses them.
def remove_namespaces(xml):
    for elem in xml.getiterator():
        split_tag = elem.tag.split('}')
        if len(split_tag) > 1:
            elem.tag = split_tag[1] 
    return xml 

if __name__ == '__main__':
    main()
