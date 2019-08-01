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

#Code for Q1
url='http://<Replace for Q1>/<Replace for Q1>'
switchuser='<Replace for Q1>'
switchpassword='<Replace for Q1>'
headers={'content-type':'application/<Replace for Q1>'}

#The CLI commands to configure an interface to be administratively up are:
#configure terminal
#interface <name>
#no shutdown
#end

#Enter the commands below, at <Replace for Q1>, to configure the Ethernet 4/1 interface to be administratively up.
payload={
  "ins_api": {
    "version": "1.2",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "interface <Replace for Q1> ; no <Replace for Q1>",
    "output_format": "json"
  }
}
response = requests.<Replace for Q1>(url, data=json.dumps(payload), headers=headers, auth=(switchuser, switchpassword)).json()
#The following line may be uncommented for debug purposes
#print(json.dumps(response,sort_keys=True,indent=4, separators=(',', ': ')))
#Replace the final dictionary key with the apppropriate value for the code representing the results of the operation
print("codes are " + response['ins_api']['outputs']['output'][0]['<Replace for Q1>'] + " and " + response['ins_api']['outputs']['output'][1]['<Replace for Q1>'])

#End of code for Q1

#Code for Q2

#Enter the commands below, at <Replace for Q2>, to show the interface Ethernet 4/1 details.
payload={
  "ins_api": {
    "version": "1.2",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show <Replace for Q2> <Replace for Q2>",
    "output_format": "json"
  }
}
response = requests.<Replace for Q2>(url, data=json.dumps(payload), headers=headers, auth=(switchuser, switchpassword)).json()
#The following line may be uncommented for debug purposes
#print(json.dumps(response,sort_keys=True,indent=4, separators=(',', ': ')))
#Replace the final dictionary key with the apppropriate value for the state of the interface
print("state is " + response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['<Replace for Q2>'])
#End of code for Q2
