class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

if __name__ == "__main__":
    p1 = Person('Juan')
    print(p1.name, p1.age)
    p2 = Person('Carlos', 10)
    print(p2.name, p2.age)
