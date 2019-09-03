m = 7

def m1():
    m = 5
    print(m)

def m2():
    global m
    m = 4
    print(m)

def m3():
    m = 6
    print(m)
    m2()

def m4():
    print(m)

m1()
m2()
m3()
m2()

m4()

m = 9

m2()
m1()

print(m)