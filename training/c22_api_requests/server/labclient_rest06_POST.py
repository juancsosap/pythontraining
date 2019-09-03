import requests


def printtask(task):
    print('ID:          {}'.format(task['id']))
    print('Title:       {}'.format(task['title']))
    print('Description: {}'.format(task['description']))
    print('Done:        {}'.format(task['done']))
    print()


def main():
    url = 'http://localhost/api/v1/tasks'
    headers = {'Accept': 'application/json'}
    payload = {'title': 'Make the Food',
               'description': 'Prepare something to eat'}

    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        task = response.json()['task']
        printtask(task)
    else:
        print(response.content.decode('UTF-8'))


if __name__ == '__main__':
    main()
