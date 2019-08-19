class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def print(self, text):
        print(text, self.name, self.age)

if __name__ == "__main__":
    p1 = Person('Juan')
    p1.print('P1:')
    p2 = Person('Carlos', 10)
    p2.print('P2:')
