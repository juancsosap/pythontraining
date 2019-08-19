class Person:
    def __init__(self, name, age=0, male=True):
        self.set_name(name)
        self.set_age(age)
        self.set_gender(male)
    
    # Setter for name field
    def set_name(self, value):
        if(isinstance(value, str)):
            if(len(value) >= 3 and len(value) <= 100):
                self.__name = value
                return
        raise ValueError
            
    # Getter for name field
    def get_name(self):
        return self.__name

    # Setter for age field
    def set_age(self, value):
        if(isinstance(value, int)):
            if(value >= 0 and value < 150):
                self.__age = value
                return
        raise ValueError
    
    # Getter for age field
    def get_age(self):
        return self.__age
    
    # Setter for male field
    def set_gender(self, value):
        if(isinstance(value, bool)):
            self.__male = value
            return
        raise ValueError

    # Getter for male field
    def is_male(self):
        return self.__male

    # Getter for male field
    def get_gender(self):
        return 'M' if self.__male else 'F'

    def print(self, text):
        print(text, self.__name, self.__age, '({})'.format(self.get_gender()))

if __name__ == "__main__":
    p1 = Person('Juan')
    p1.print('P1:')
    p2 = Person('Carlos', 10)
    p2.print('P2:')
    p3 = Person('Ana', male=False)
    p3.print('P3:')
    p4 = Person('Gabriela', 15, False)
    p4.print('P4:')
    
    p1.print('P1:')
    print(dir(p1))

    # Create dinamically a new field
    p1.__name = 'Luis'
    
    p1.print('P1:')
    print(dir(p1))

    # Shorcut to access private fields and methods
    p1._Person__name = 'Luis'
    p1.print('P1:')
