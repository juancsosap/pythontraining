import requests


def main():
    url = 'http://httpbin.org/get?name=juan&age=35'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        print(content.decode('utf-8'))


if __name__ == '__main__':
    main()