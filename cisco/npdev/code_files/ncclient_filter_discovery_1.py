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
    
            xe_intf_filter = """<native xmlns="http://cisco.com/ns/yang/ned/ios"><interface></interface></native>"""

            result = xe_device.get(('subtree', xe_intf_filter))

            print (etree.tostring(result.data_ele, pretty_print=True))

    if try_xr:
        with manager.connect(host='xrv', port=830, username=xr_user, password=xr_pass, device_params={'name' : 'iosxr'}, allow_agent=False, look_for_keys=False, hostkey_verify=False) as xr_device:

            xr_intf_filter = """<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"></interface-configurations>"""

            result = xr_device.get(('subtree', xr_intf_filter))

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

