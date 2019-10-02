import requests


def main():
    access_token = '3d47dd0b36d9aa33eeac6040d96242d20f2f28c8'

    url = 'http://api.github.com/user/repos'
    headers = {'authorization': 'token ' + access_token, 'Accept': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        for project in response_json:
            name = project['name']
            print(name)
    else:
        print(response.content.decode('UTF-8'))


if __name__ == '__main__':
    main()
