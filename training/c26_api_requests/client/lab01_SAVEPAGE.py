import requests


def main():
    url = 'https://www.google.com/'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        save('google.html', content)


def save(file, content):
    with open(file, 'wb') as file:
        file.write(content)


if __name__ == '__main__':
    main()
