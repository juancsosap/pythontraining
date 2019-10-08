import requests


def main():
    url = 'http://httpbin.org/post'
    payload = {'name': 'juan', 'age': 35}
    headers = {'content-type': 'application/json',
               'access-token': '12345'}

    response = requests.post(url, json=payload, headers=headers)
    print(response.url)
    if response.status_code == 200:
        response_headers = response.headers  # Dictionary
        print(response_headers['server'])


if __name__ == '__main__':
    main()
