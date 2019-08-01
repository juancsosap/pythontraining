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
from lxml import etree
import logging

verbose = False
    
xe_user = "cisco"
xe_pass = "cisco"
try_xe = True

xr_user = "cisco"
xr_pass = "cisco"
try_xr = True

def main():
    if verbose: set_logging()

    if try_xe:
        with manager.connect(host='csr1kv', port=830, username=xe_user, password=xe_pass, device_params={'name' : 'csr'}, allow_agent=False, look_for_keys=False, hostkey_verify=False) as xe_device:

            xe_add_interface_config = """
            <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
              <native xmlns="http://cisco.com/ns/yang/ned/ios">
                <interface>
                  <Loopback>
                    <name>101</name>
                    <ip>
                      <address>
                        <primary>
                          <address>10.101.1.1</address>
                          <mask>255.255.255.0</mask>
                        </primary>
                      </address>
                    </ip>
                  </Loopback>
                </interface>
              </native>
            </config>"""


            xe_delete_interface_config = """
            <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
              <native xmlns="http://cisco.com/ns/yang/ned/ios">
                <interface>
                  <Loopback nc:operation="delete">
                    <name>101</name>
                  </Loopback>
                </interface>
              </native>
            </config>"""

            xe_intf_filter = """<native xmlns="http://cisco.com/ns/yang/ned/ios"><interface></interface></native>"""

            print("**Trying the IOS XE device*\n")
            
            print("\nShow which interfaces exist. There should only be one GigabitEthernet interface.\n**")
            filter_result = xe_device.get(('subtree', xe_intf_filter))
            print (etree.tostring(filter_result.data_ele, pretty_print=True))

            print("\nAdd a Loopback interface.\n**")
            add_result = xe_device.edit_config(target="running", config=xe_add_interface_config, default_operation="merge")
            print (add_result)
            
            print("\nShow that the Loopback interface has been added.\n**")
            filter_result = xe_device.get(('subtree', xe_intf_filter))
            print (etree.tostring(filter_result.data_ele, pretty_print=True))

            print("\nDelete the Loopback interface.\n**")
            delete_result = xe_device.edit_config(target="running", config=xe_delete_interface_config)
            print (delete_result)

            print("\nShow that the Loopback interface has been deleted.\n**")
            filter_result = xe_device.get(('subtree', xe_intf_filter))
            print (etree.tostring(filter_result.data_ele, pretty_print=True))


    if try_xr:
        with manager.connect(host='xrv', port=830, username=xr_user, password=xr_pass, device_params={'name' : 'iosxr'}, allow_agent=False, look_for_keys=False, hostkey_verify=False) as xr_device:

            xr_add_interface_config = """
            <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
              <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
                <interface-configuration>
                  <active>act</active>
                  <interface-name>Loopback100</interface-name>
                  <interface-virtual/>
                </interface-configuration>
              </interface-configurations>
            </config>"""

            xr_delete_interface_config = """
            <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
              <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
                <interface-configuration nc:operation="delete">
                  <active>act</active>
                  <interface-name>Loopback100</interface-name>
                </interface-configuration>
              </interface-configurations>
            </config>"""

            xr_intf_filter = """<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"></interface-configurations>"""

            print("**Trying the IOS XR device**\n")
            
            print("\nShow which interfaces exist. There should only be one Management interface.\n**")
            filter_result = xr_device.get(('subtree', xr_intf_filter))
            print (etree.tostring(filter_result.data_ele, pretty_print=True))

            print("\nAdd a Loopback interface.\n**")
            add_result = xr_device.edit_config(target='candidate', config=xr_add_interface_config, default_operation="merge")
            print (add_result)
            xr_device.commit()
            
            print("\nShow that the Loopback interface has been added.\n**")
            filter_result = xr_device.get(('subtree', xr_intf_filter))
            print (etree.tostring(filter_result.data_ele, pretty_print=True))

            print("\nDelete the Loopback interface.\n**")
            delete_result = xr_device.edit_config(target="candidate", config=xr_delete_interface_config)
            xr_device.commit()
            print (delete_result)

            print("\nShow that the Loopback interface has been deleted.\n**")
            filter_result = xr_device.get(('subtree', xr_intf_filter))
            print (etree.tostring(filter_result.data_ele, pretty_print=True))

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

