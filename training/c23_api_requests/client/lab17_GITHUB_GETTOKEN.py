import requests


def main():
    clientID = 'f3f8c27351ee3dccdcc6'

    # https://github.com/login/oauth/authorize?client_id=f3f8c27351ee3dccdcc6&scope=repo
    url = 'https://github.com/login/oauth/authorize'

    # It return a code
    code = '59b486ff862b314ab382'

    clientSecret = '202fc68969214f9597354dd09ffadc041e8c1b16'
    access_token = ''

    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id': clientID, 'client_secret': clientSecret, 'code': code}
    headers = {'Accept': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json.get('access_token', '')
        print(access_token)


if __name__ == '__main__':
    main()
