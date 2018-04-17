import requests


def main():
    url = 'http://pokeapi.co/api/v2/pokemon-form/'

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        payload = response.json()
        print(payload)


if __name__ == '__main__':
    main()
