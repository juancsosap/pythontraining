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

#Code for Q1.
#The name of the VLAN media type element in the output from a show command for a VLAN is:
#vlanshowinfo-media-type

import cisco
cli('configure terminal ; vlan 3000 ; name vlan_3000 ')
cli('end ')

vlan_text = clid('show vlan name vlan_3000 ')
#Print the value of the VLAN media type
for pair in vlan_text.split(',') :
  if 'vlanshowinfo-media-type' in pair:
    result = pair[pair.index(':')+2:len(pair)]
    print("result is " + result)

cli('configure terminal ; no vlan 3000 ')
cli('end ')
#Press return here to complete configuration change
#End of code for Q1

#Code for Q2.
#The name of the Administrative State Reason is:
#state_rsn_desc

import cisco

cli('configure terminal ; interface Ethernet4/38 ; no shutdown ')
cli('end ')

interface_text = clid('show interface Ethernet4/38 ')

#Print the value of the Administrative State Reason
for pair in interface_text.split(',') :
  if 'state_rsn_desc' in pair:
    result = pair[pair.index(':')+2:len(pair)]
    print("result is " + result)

#Press return here to see result

#End of code for Q2
    



