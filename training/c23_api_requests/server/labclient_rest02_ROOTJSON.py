import requests


def main():
    url = 'http://localhost/'
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.ok:
        print(response.json()['message'])
    else:
        print(response.content.decode('UTF-8'))


if __name__ == '__main__':
    main()
