import requests
import json


def main():
    url = 'http://httpbin.org/post'
    payload = {'name': 'juan', 'age': 35}
    data = json.dumps(payload)

    # when the data is send usin 'DATA' keyword
    # the post method require the data serialized
    response = requests.post(url, data=data)
    print(response.url)
    if response.status_code == 200:
        print(response.content.decode('UTF-8'))


if __name__ == '__main__':
    main()
