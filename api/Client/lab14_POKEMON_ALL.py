import requests


def main():
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    count = 1

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            payload = response.json()
            results = payload.get('results', [])

            if results:
                for pokemon in results:
                    name = pokemon['name']
                    print(str(count) + ':' + name)
                    count += 1

            url = payload['next']


if __name__ == '__main__':
    main()
