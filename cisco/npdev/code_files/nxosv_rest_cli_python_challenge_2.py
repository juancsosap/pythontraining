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

import requests
import json


#Code for Q3
url='http://nxosv/<Replace for Q3>'
switchuser='<Replace for Q3>'
switchpassword='<Replace for Q3>'
headers={'content-type':'<Replace for Q3>json'}

#The CLI commands to configure BGP with an IPv6 unicast address family and network of 2001:DB8::/32 are:
#configure terminal
#router bgp <autonomous-system-number>, e.g. 64496
#address-family ipv6 unicast
#network 2001:DB8::/32
#end

#Enter the commands below, at <Replace for Q3>, to configure BGP with an IPv6 unicast address family and network of 2001:DB8::/32.
payload={
  "ins_api": {
    "version": "1.2",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "router <Replace for Q3> 64496 ;address-family <Replace for Q3> unicast ;<Replace for Q3> 2001:DB8::/32",
    "output_format": "json"
  }
}
response = requests.<Replace for Q3>(url, data=json.dumps(payload), headers=headers, auth=(switchuser, switchpassword)).json()
#The following line may be uncommented for debug purposes
#print(json.dumps(response,sort_keys=True,indent=4, separators=(',', ': ')))
#Replace the final dictionary key with the apppropriate value for the message representing the results of the operation
print("messages are " + response['ins_api']['outputs']['output'][0]['<Replace for Q3>'] + ", " + response['ins_api']['outputs']['output'][1]['<Replace for Q3>'] + " and " + response['ins_api']['outputs']['output'][2]['<Replace for Q3>'])


#End of code for Q3

#Code for Q4

#Enter the commands below, at <Replace for Q4>, to show all bgp details.
payload={
  "ins_api": {
    "version": "1.2",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show bgp <Replace for Q4>",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=headers,auth=(switchuser, switchpassword)).json()
#The following line may be uncommented for debug purposes
#print(json.dumps(response,sort_keys=True,indent=4, separators=(',', ': ')))
#Replace the final dictionary key with the apppropriate value for the best path value.
print("best is " + response['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi'][1]['TABLE_safi']['ROW_safi']['TABLE_rd']['ROW_rd']['TABLE_prefix']['ROW_prefix']['TABLE_path']['ROW_path']['<Replace for Q4>'])

#End of code for Q4
