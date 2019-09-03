basedir = __file__[:__file__.rfind('/')+1]

import json

path = basedir + 'docs/data.json'

with open(path) as file:
    text = file.read()
    print(text)
    
    print()

    config = json.loads(text)
    print(type(config))
    print(dir(config))
    print(config)
    print(config.get('name', None))

    print()

    doc = json.dumps(config)
    print(type(doc))
    print(doc)
