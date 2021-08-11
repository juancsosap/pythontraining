import requests, os, urllib3, json

basedir = __file__[:__file__.rfind('\\')+1]
if basedir != '': os.chdir(basedir)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def rest_request(baseurl, filename):
    urlauth = f'{baseurl}/xmlapi/invoke'
    body = open(f'requests/{filename}').read()
    headers = {'content-type': 'text/xml'}
    response = requests.post(url, data=body, headers=headers, verify=False)
    
    if response.status_code == 200:
        result = response.content.decode(response.encoding)   
        print('Done Successfully')
        print(result)
    else:
        print(f'Error {response.status_code}: {response.reason}')
    
if __name__ == "__main__":
    url = 'https://10.127.39.242'
    rest_request(url, 'ping.xml')
    
