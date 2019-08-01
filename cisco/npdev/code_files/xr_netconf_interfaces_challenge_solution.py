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
import logging

def main():

    #set_logging()

    print("Start Q1.\n**")
    
    with manager.connect(host='xrv', port=830, username='cisco', password='cisco', 
                         hostkey_verify=False, device_params={'name': 'iosxr'}, 
                         allow_agent=False, look_for_keys=False) as xr_device: 

        nc_interface_filter = """ 
              <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
               <interface-configuration> 
               </interface-configuration> 
              </interface-configurations>"""

        print("Tying nc_interface_filter\n**" )
        nc_get_reply = xr_device.get(('subtree', nc_interface_filter)) 
        print(nc_get_reply)

        print("End Q1.\n**")

        print("Start Q2.\n**")

        print("Add GigabitEthernet0/0/0/0 interface with primary address \"10.23.23.1 255.255.255.0\" and a secondary address \"20.32.32.1, 255.255.255.0\".\n**")

        nc_add_interface_config = """ 
            <config> 
             <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
               <interface-configuration> 
                <active>act</active> 
                <interface-name>GigabitEthernet0/0/0/0</interface-name> 
                <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg"> 
                 <addresses> 
                  <primary> 
                   <address>10.23.23.1</address> 
                   <netmask>255.255.255.0</netmask> 
                  </primary> 
                  <secondaries> 
                   <secondary> 
                    <address>20.32.32.1</address> 
                    <netmask>255.255.255.0</netmask> 
                   </secondary> 
                  </secondaries> 
                 </addresses> 
                </ipv4-network> 
                <shutdown></shutdown> 
               </interface-configuration> 
              </interface-configurations> 
            </config> 
        """

        nc_reply = xr_device.edit_config(target='candidate', config=nc_add_interface_config, default_operation="merge") 
        print(nc_reply) 
        xr_device.commit()
        print("Tying nc_interface_filter\n**" )
        nc_get_reply = xr_device.get(('subtree', nc_interface_filter)) 
        print(nc_get_reply)

        print("End Q2.\n**")

        print("Start Q3.\n**")

        print("Tying nc_gig0000_interface_filter\n**" )

        #Note that the interface has been added as a pre-configured interface, because there is no NIC yet.
        #Hence the value of the "active" field is "pre"
        
        nc_gig0000_interface_filter = """ 
              <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
               <interface-configuration>
                <active>pre</active> 
                <interface-name>GigabitEthernet0/0/0/0</interface-name> 
               </interface-configuration> 
              </interface-configurations>"""

        nc_get_reply = xr_device.get(filter=('subtree', nc_gig0000_interface_filter)) 
        print(nc_get_reply)

        print("End Q3.\n**")

        print("Start Q4.\n**")

        print("Delete secondary address \"20.32.32.1, 255.255.255.0\" from the GigabitEthernet0/0/0/0 interface.\n**")

        nc_delete_address_config = """ 
            <config> 
             <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
               <interface-configuration> 
                <active>pre</active> 
                <interface-name>GigabitEthernet0/0/0/0</interface-name> 
                <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg"> 
                 <addresses> 
                  <secondaries>
                    <secondary nc:operation="delete"> 
                     <address>20.32.32.1</address> 
                     <netmask>255.255.255.0</netmask> 
                   </secondary> 
                  </secondaries>
                 </addresses> 
                </ipv4-network> 
               </interface-configuration> 
              </interface-configurations> 
            </config>"""
        
        nc_reply = xr_device.edit_config(target='candidate', config=nc_delete_address_config) 
        print(nc_reply) 
        xr_device.commit()

        print("Expect to see only the primary address for the GigabitEthernet0/0/0/0 interface. \n**") 
        nc_get_reply = xr_device.get(('subtree', nc_gig0000_interface_filter)) 
        print(nc_get_reply)

        print("End Q4.\n**")

def set_logging():
    LOGGING_TO_ENABLE = [
        'ncclient.transport.ssh',
        'ncclient.transport.session',
        'ncclient.operations.rpc'
    ]

    handler = logging.StreamHandler()
    for l in LOGGING_TO_ENABLE:
        logger = logging.getLogger(l)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    main()
