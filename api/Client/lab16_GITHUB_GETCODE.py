import requests


def main():
    clientID = 'f3f8c27351ee3dccdcc6'

    # https://github.com/login/oauth/authorize?client_id=f3f8c27351ee3dccdcc6&scope=repo
    url = 'https://github.com/login/oauth/authorize'
    args = {'client_id': clientID, 'scope': 'repo'}

    response = requests.get(url, params=args)
    if response.status_code == 200:
        pass

    # It return a code


if __name__ == '__main__':
    main()
