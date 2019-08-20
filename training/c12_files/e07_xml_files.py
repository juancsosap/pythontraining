import xml.etree.ElementTree as et

tree = et.parse('docs/data.xml')
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

root.write
text = et.tostring(root)
print(text)