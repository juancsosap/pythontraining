import requests


def main():
    url = 'http://httpbin.org/post'
    payload = {'name': 'juan', 'age': 35}

    # when the data is send usin 'JSON' keyword
    # the post method automatically serialize the data
    response = requests.post(url, json=payload)
    print(response.url)
    if response.status_code == 200:
        print(response.content.decode('UTF-8'))


if __name__ == '__main__':
    main()
