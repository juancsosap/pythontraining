import json

with open('docs/data.json') as file:
    text = file.read()
    print(text)
    
    print()

    config = json.loads(text)
    print(type(config))
    print(dir(config))
    print(config)

    print()

    doc = json.dumps(config)
    print(type(doc))
    print(doc)
