import requests


def main():
    url = 'http://httpbin.org/get'
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()  # Dictionary
        origin = response_json['origin']
        print(origin)


if __name__ == '__main__':
    main()
