import requests


def main():
    url = 'http://httpbin.org/put'
    payload = {'name': 'juan', 'age': 35}
    headers = {'content-type': 'application/json',
               'access-token': '12345'}

    response = requests.put(url, json=payload, headers=headers)
    print(response.url)
    if response.status_code == 200:
        print(response.content.decode('UTF-8'))


if __name__ == '__main__':
    main()
