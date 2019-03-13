import requests


def main():
    url = 'http://api.github.com/user'
    session = requests.session()
    session.auth = ('juan.c.sosa.p@gmail.com', 'Ed1d3n5Valcrost-217-Github')
    response = session.get(url)

    if response.ok:
        url = 'https://github.com/juancsosap/javatraining'
        response = session.get(url)
        if response.ok:
            print(response.content.decode('UTF-8'))
            print(response.cookies)


if __name__ == '__main__':
    main()
