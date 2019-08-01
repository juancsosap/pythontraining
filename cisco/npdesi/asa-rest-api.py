#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

# GET REQUEST - Get Info

url = 'https://asa/api/monitoring/device/components/version'

auth = HTTPBasicAuth('cisco', 'cisco')

response = requests.get(url, verify=False, auth=auth)

if response.status_code == 200:
	print 'Status Code:', str(response.status_code)
	parse = json.loads(response.text)
	print json.dumps(parse, indent=4)
else:
	print 'ERROR Code:', str(response.status_code)

"""
cisco@cisco:~$ python show_version.py
Status Code: 200
{
	"kind": "object#Version",
	"currentTimeinSeconds": 1468510065,
	"asaVersion": "9.5(2)207",
	"totalFlashinMB": 8192,
	"deviceType": "ASAv",
	"upTimeinSeconds": 802800,
	"firewallMode": "Router",
	"selfLink": "/api/monitoring/device/version"
}
"""

# POST REQUEST - Create Object

url = 'https://asa/api/objects/networkobjects'

payload = {
	"host": {
		"kind": "IPv4Address",
		"value": "10.10.10.110"
	},
	"kind": "object#NetworkObj",
	"name": "web_server08",
	"objectId": "web_server08"
}

headers = {
	"content-type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False, auth=auth)

if response.status_code == 201:
	print 'Status Code:', str(response.status_code)
else:
	print 'ERROR Code:', str(response.status_code)

print response.headers

"""
cisco@cisco:~$ python push_object.py
Status Code: 201
{'Content-length': '0', 'Accept-ranges': 'bytes', 'Vary': 'Accept-Charset, Accept-Encoding, Accept-Language, Accept', 'Server': 'CiscoASARestApiServer', 'Location': 'https://asa/api/objects/networkobjects/web_server08', 'Date': 'Thu, 14 Jul 2016 18:08:41 GMT'}
"""