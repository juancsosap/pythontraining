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
#
# Generated ASA REST API sample script - Python 2.7
#

import base64
import json
import sys
import urllib2
# Uncomment the following two lines, if you are using Python 2.7.9 or above to connect to an ASA with a self-signed certificate.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

server = "https://asa"

username = "cisco"
if len(sys.argv) > 1:
    username = sys.argv[1]
password = "cisco"
if len(sys.argv) > 2:
    password = sys.argv[2]


headers = {'Content-Type': 'application/json'}

tokenservices_api_path = "/api/monitoring/connections"
monitoring_api_path = "/api/monitoring/connections"

url = server + tokenservices_api_path
f = None

# GET OPERATION


req = urllib2.Request(url, None, headers)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string)
try:
    f = urllib2.urlopen(req)
    status_code = f.getcode()
    if (status_code != 200):
        print 'Error in get. Got status code: '+status_code
    resp = f.read()
    json_resp = json.loads(resp)
    print json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': '))
finally:
    if f:  f.close()
