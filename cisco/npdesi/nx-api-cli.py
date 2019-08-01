#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":

	auth = HTTPBasicAuth('cisco', 'cisco')

	headers = {
		"content-type": "application/json"
	}

	payload = {
		"ins_api": {
			"version": "1.0",
			"type": "cli_show",
			"chunk": "0",
			"sid": "1",
			"input": "show version",
			"output_format": "json"
		}
	}

	url = 'http://nxosv/ins'

	response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)

	if response.status_code == 201:
		print 'Status Code:', str(response.status_code)
		parse = json.loads(response.text)
		print json.dumps(parse, indent=4)
	else:
		print 'ERROR Code:', str(response.status_code)

	print response.headers