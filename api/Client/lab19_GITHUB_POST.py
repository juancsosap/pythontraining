import requests


def main():
    access_token = '3d47dd0b36d9aa33eeac6040d96242d20f2f28c8'

    url = 'http://api.github.com/user/repos'
    headers = {'authorization': 'token ' + access_token, 'Accept': 'application/json'}
    payload = {'name': 'api-testing'}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.content.decode('UTF-8'))


if __name__ == '__main__':
    main()
