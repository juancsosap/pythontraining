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

    print("Start Q1.\n**")

    with manager.connect(host='<Replace for Q1>', port=<Replace for Q1>, username='<Replace for Q1>', password='<Replace for Q1>',
                         hostkey_verify=False, device_params={'name': '<Replace for Q1>'},
                         allow_agent=False, look_for_keys=False) as nxosv:

        #The commands to enable the VLAN feature and configure a VLAN with an ID of 300 and an address of 198.51.100.10/24 are:
        # nxosv# configure terminal
        # nxosv(config)# feature interface-vlan
        # nxosv(config)# interface vlan 300
        # nxosv(config-if)# ip address 198.51.100.10/24
        # nxosv(config-if)# end
        vlan_300_commands = ['configure terminal', 'feature <Replace for Q1>', 'interface <Replace for Q1> 300', 'ip <Replace for Q1> 198.51.100.10/24']
        nc_config_reply = nxosv.exec_command(vlan_300_commands)
        print(nc_config_reply)

        print("End Q1.\n**")

        print("Start Q2.\n**")

        ##Use this command at the NXOSv CLI to get the XML element name for the interface ID in the filter (use the part after '__XML__PARAM__'):
        #show interface vlan 300 | xmlin
        show_interface_vlan_300_filter = """<show><interface><<Replace for Q2>>Vlan300</<Replace for Q2>></interface></show>"""
        nc_get_reply = nxosv.get(('subtree', show_interface_vlan_300_filter))
        nc_get_reply_no_ns = remove_namespaces(nc_get_reply.data_ele)
        #Use this command at the NXOSv CLI to get the XML element name for the IP address mask:
        #show interface vlan 300 | xmlout
        print("Mask value is - " + nc_get_reply_no_ns.find('.//' + '<Replace for Q2>').text)

        print("End Q2.\n**")

#The namespaces in the XML response make life awkward, so this function cleanses them.
def remove_namespaces(xml):
    for elem in xml.getiterator():
        split_tag = elem.tag.split('}')
        if len(split_tag) > 1:
            elem.tag = split_tag[1] 
    return xml 

if __name__ == '__main__':
    main()
