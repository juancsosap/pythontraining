import requests


def main():
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    count, offset = 0, 0
    index = 1

    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        count = payload['count']

    for offset in range(0, count, 20):
        args = {'offset': offset}
        response = requests.get(url, params=args)
        if response.status_code == 200:
            payload = response.json()
            results = payload.get('results', [])

            if results:
                for pokemon in results:
                    name = pokemon['name']
                    print(str(index) + ':' + name)
                    index += 1


if __name__ == '__main__':
    main()
