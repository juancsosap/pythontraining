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
    
    # with manager.connect(host='<REPLACE for Q1>', port=<REPLACE for Q1>, username='<REPLACE for Q1>', password='<REPLACE for Q1>', 
    #                      hostkey_verify=False, device_params={'name': '<REPLACE for Q1>'}, 
    #                      allow_agent=False, look_for_keys=False) as xr_device: 

    #     nc_interface_filter = """ 
    #     <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
    #       <interface-configuration> 
    #       </interface-configuration> 
    #     </interface-configurations>"""
        
    #     print("Trying nc_interface_filter\n**" )
    #     nc_get_reply = xr_device.<REPLACE for Q1>(('<REPLACE for Q1>', <REPLACE for Q1>)) 
    #     print(nc_get_reply) 

        #print("End Q1.\n**")

        #print("Start Q2.\n**")

        # print("Add GigabitEthernet0/0/0/0 interface with primary address \"10.23.23.1, 255.255.255.0\" and a secondary address \"20.32.32.1, 255.255.255.0\".\n**")
        
        # nc_add_interface_config = """ 
        # <config> 
        #   <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
        #     <interface-configuration> 
        #       <active>act</active> 
        #       <interface-name><REPLACE for Q2></interface-name> 
        #       <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg"> 
        #         <addresses> 
        #           <primary> 
        #             <address><REPLACE for Q2></address> 
        #             <netmask><REPLACE for Q2></netmask> 
        #           </primary> 
        #           <secondaries> 
        #             <secondary> 
        #               <address><REPLACE for Q2></address> 
        #               <netmask><REPLACE for Q2></netmask> 
        #             </secondary> 
        #           </secondaries> 
        #         </addresses> 
        #       </ipv4-network> 
        #       <shutdown></shutdown> 
        #     </interface-configuration> 
        #   </interface-configurations> 
        # </config> 
        # """
           
        # nc_reply = xr_device.<REPLACE for Q2>(target='<REPLACE for Q2>', config=<REPLACE for Q2>, default_operation="<REPLACE for Q2>") 
        # print(nc_reply) 
        # xr_device.commit()
        # print("Trying nc_interface_filter\n**" )
        # nc_get_reply = xr_device.<REPLACE for Q2>(('<REPLACE for Q2>', <REPLACE for Q2>))  
        # print(nc_get_reply)

        #print("End Q2.\n**")

        #print("Start Q3.\n**")

        # print("Trying nc_gig0000_interface_filter\n**" )

        #Note that the interface has been added as a pre-configured interface, because there is no NIC yet.
        #Hence the value of the "active" field is "pre"
        
        # nc_gig0000_interface_filter = """ 
        # <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
        #   <interface-configuration>
        #     <active>pre</active> 
        #     <interface-name><REPLACE for Q3></interface-name> 
        #   </interface-configuration> 
        # </interface-configurations>"""
        
        #nc_get_reply = xr_device.<REPLACE for Q3>(filter=('<REPLACE for Q3>', nc_gig0000_interface_filter)) 
        #print(nc_get_reply)

        #print("End Q3.\n**")

        #print("Start Q4.\n**")

        # print("Delete secondary address \"20.32.32.1, 255.255.255.0\" from the GigabitEthernet0/0/0/0 interface.\n**")

        # nc_delete_address_config = """ 
        # <config> 
        #   <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
        #     <interface-configuration> 
        #       <active>pre</active> 
        #       <interface-name><REPLACE for Q4></interface-name> 
        #       <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg"> 
        #         <addresses> 
        #           <secondaries>
        #             <secondary nc:operation="<REPLACE for Q4>"> 
        #               <address><REPLACE for Q4></address> 
        #               <netmask><REPLACE for Q4></netmask> 
        #             </secondary> 
        #           </secondaries>
        #         </addresses> 
        #       </ipv4-network> 
        #     </interface-configuration> 
        #   </interface-configurations> 
        # </config>"""
        
        # nc_reply = xr_device.<REPLACE for Q4>(target='candidate', config=<REPLACE for Q4>) 
        # print(nc_reply) 
        # xr_device.commit()
        
        # print("Expect to see only the primary address for the GigabitEthernet0/0/0/0 interface. \n**") 
        # nc_get_reply = xr_device.<REPLACE for Q4>(('<REPLACE for Q4>', <REPLACE for Q4>)) 
        # print(nc_get_reply)

        #print("End Q4.\n**")

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
