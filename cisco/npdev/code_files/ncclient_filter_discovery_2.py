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

            xe_enable_snmp_traps_config = """ 
            <config>
              <netconf-yang xmlns="http://cisco.com/yang/cisco-self-mgmt">
                <cisco-ia xmlns="http://cisco.com/yang/cisco-ia">
                  <snmp-trap-control>
                    <trap-list>
                      <trap-oid>1.3.6.1.4.1.9.9.41.2.0.1</trap-oid>
                    </trap-list>
                    <trap-list>
                      <trap-oid>1.3.6.1.6.3.1.1.5.3</trap-oid>
                    </trap-list>
                    <trap-list>
                      <trap-oid>1.3.6.1.6.3.1.1.5.4</trap-oid>
                    </trap-list>
                  </snmp-trap-control>
                </cisco-ia>
              </netconf-yang>
            </config>"""

            xe_configure_odm_config = """
            <config>
              <netconf-yang xmlns="http://cisco.com/yang/cisco-self-mgmt">
                <cisco-odm xmlns="http://cisco.com/yang/cisco-odm">
                  <polling-enable>true</polling-enable>
                  <on-demand-default-time>30000</on-demand-default-time>
                  <on-demand-enable>false</on-demand-enable>
                  <actions>
                    <action-name>parse.showACL</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showArchive</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showEnvironment</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showFlowMonitor</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showInterfaces</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showIpRoute</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showMemoryStatistics</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showPlatformSoftware</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showProcessesCPU</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                  <actions>
                    <action-name>parse.showProcessesMemory</action-name>
                    <polling-interval>120000</polling-interval>
                    <mode>poll</mode>
                  </actions>
                </cisco-odm>
              </netconf-yang>
            </config>"""
            
            xe_device.edit_config(target="running",config=xe_enable_snmp_traps_config, default_operation="merge")
            xe_device.edit_config(target="running",config=xe_configure_odm_config, default_operation="merge")

            xe_operational_filter = """<interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"></interfaces-state>"""

            result = xe_device.get(('subtree', xe_operational_filter))

            print (etree.tostring(result.data_ele, pretty_print=True))

    if try_xr:
        with manager.connect(host='xrv', port=830, username=xr_user, password=xr_pass, device_params={'name' : 'iosxr'}, allow_agent=False, look_for_keys=False, hostkey_verify=False) as xr_device:

            xr_operational_filter = """<interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper"><interface-xr><interface><interface-name>MgmtEth0/0/CPU0/0</interface-name></interface></interface-xr></interfaces>"""

            result = xr_device.get(('subtree', xr_operational_filter))

            print (etree.tostring(result.data_ele, pretty_print=True))

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

    
