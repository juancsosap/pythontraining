import requests


def printtask(task):
    print('ID:          {}'.format(task['id']))
    print('Title:       {}'.format(task['title']))
    print('Description: {}'.format(task['description']))
    print('Done:        {}'.format(task['done']))
    print()


def main():
    url = 'http://localhost/api/v1/tasks/3'
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.ok:
        task = response.json()['task']
        printtask(task)
    else:
        print(response.json()['error'])


if __name__ == '__main__':
    main()
