import requests
import json

def get_cookies(apic):
	url = apic + '/api/aaaLogin.json'
	auth = { 
		"aaaUser": {
			"name": "admin",
			"pwd": "cisco123"
		}
	}
	authenticate = requests.post(url, data=json.dumps(auth), verify=False)
	return authenticate.cookies

def get_subnets(apic, cookies):
	uri = '/api/class/fvSubnet.json'
	url = apic + uri
	req = requests.get(url, cookies=cookies, verify=False)
	response = req.text
	return response

if __name__ == "__main__":
	apic = 'http://apic'
	cookies = get_cookies(apic)

	rsp = get_subnets(apic,cookies)
	rsp_dict = json.loads(rsp)
	subnets = rsp_dict['imdata']