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

url = "https://apic-em:443/api/v1/ticket"

payload = "{ \n    \"username\" : \"admin\",\n\"password\" : \"Cisco123!\"\n}\n"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "1a5df2dc-23ed-7856-cde3-42c22780fc52"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)
