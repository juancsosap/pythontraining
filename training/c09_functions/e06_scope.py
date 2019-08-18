class Box:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

def printer1(box):
    box.value = 'method 1'
    print(box)

def printer2():
    box.value = 'method 2'
    print(box)

def printer3():
    box = Box('method 3')
    print(box)

def printer4():
    global box
    box = Box('method 4')
    print(box)

box = Box('global')

print(box)
printer1(box)
print(box)

print('----------')

box = Box('global')

print(box)
printer2()
print(box)

print('----------')

box = Box('global')

print(box)
printer3()
print(box)

print('----------')

box = Box('global')

print(box)
printer4()
print(box)
