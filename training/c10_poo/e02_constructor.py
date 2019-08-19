class Person:
    def __init__(self):
        print('Calling Constructor')
        print(self)
    
    def __del__(self):
        print('Calling Distructor')
        

if __name__ == "__main__":
    p1 = Person()
    p2 = Person()

    del p1

    p3 = Person()
