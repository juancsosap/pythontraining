import requests


def main():
    url = 'http://httpbin.org/cookies'
    cookies = {'my-cookie': 'true'}

    response = requests.get(url, cookies=cookies)

    if response.ok:
        cookies = response.cookies
        content = response.content
        print(cookies)
        print(content.decode('UTF-8'))


if __name__ == '__main__':
    main()
