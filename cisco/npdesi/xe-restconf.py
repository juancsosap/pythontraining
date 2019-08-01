#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":

	auth = HTTPBasicAuth('cisco', 'cisco')

	headers = {
		"content-type": "application/vnd.yang.data+json"
		"Accept": "application/vnd.yang.data+json"
	}

	url = 'http://csr1kv/restconf/api/config/native/ip/route?deep'

	response = requests.post(url, verify=False, headers=headers, auth=auth)

	if response.status_code == 201:
		print 'Status Code:', str(response.status_code)
		parse = json.loads(response.text)
		print json.dumps(parse, indent=4)
	else:
		print 'ERROR Code:', str(response.status_code)

	print response.headers

"""
{
	"ned:route": {
		"ip-route-interface-forwarding-list": [
			{
				"fwd-list": [ { "fwd": "192.168.1.1" } ],
				"prefix": "0.0.0.0",
				"mask": "0.0.0.0"
			},
			{
				"fwd-list": [ { "fwd": "192.168.1.1" } ],
				"prefix": "172.16.0.0",
				"mask": "255.255.0.0"
			}
		],
		"static": {}
	}
}
"""