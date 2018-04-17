import requests


def printtask(task):
    print('ID:          {}'.format(task['id']))
    print('Title:       {}'.format(task['title']))
    print('Description: {}'.format(task['description']))
    print('Done:        {}'.format(task['done']))
    print('URI:         {}'.format(task['uri']))
    print()


def main():
    url = 'http://localhost/api/v1/tasks'
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.ok:
        tasks = response.json()['tasks']
        for task in tasks:
            printtask(task)
    else:
        print(response.content.decode('UTF-8'))


if __name__ == '__main__':
    main()
