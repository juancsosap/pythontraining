basedir = __file__[:__file__.rfind('/')+1]

import xml.etree.ElementTree as et

path = basedir + 'docs/data.xml'

tree = et.parse(path)
root = tree.getroot()

print(dir(tree))
print(dir(root))

print('---> All attributes:')
for elem in root:
    print(elem.tag, elem.text, elem.attrib)
    for subelem in elem:
        print(subelem.tag, subelem.text, subelem.attrib)

print('-'*50)

item = root[0]
print(item.tag, item.text, item.attrib)

print('-'*50)

item = tree.find('surname')
print(item.tag, item.text, item.attrib)

print('-'*50)
