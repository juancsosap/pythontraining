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
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

token_url = "https://asa/api/tokenservices"
monitoring_url = "https://asa/api/monitoring/connections"

auth = HTTPBasicAuth('cisco', 'cisco')
headers = {'Content-Type': 'application/json'}

response = requests.post(token_url, headers=headers, auth=auth, verify=False)
token = response.headers['x-auth-token']

headers = {'Content-Type': 'application/json',
           'x-auth-token': token}

response = requests.get(monitoring_url, headers=headers, verify=False)
print(response.text)
    

