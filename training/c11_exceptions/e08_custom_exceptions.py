class InvalidArgumentError(Exception):
    pass

class OutOfRangeValueError(ValueError):
    def __init__(self, message=None, min_val=0, max_val=0):
        if message is not None:
            msg = message 
        else:
            msg = 'The value must be between ' + str(min_val) + ' and ' + str(max_val)
        super().__init__(msg)

class Age:
    def __init__(self, value):
        if(isinstance(value, int)):
            val = int(value)
            if(val >= 0 and val < 150):
                self.__value = value
            else:
                raise OutOfRangeValueError(min_val=0, max_val=150)
        else:
            raise InvalidArgumentError('Age must be an Integer value')
    
    def get(self):
        return self.__value

if __name__ == "__main__":
    try:
        age = Age('25')
        print(age.get())
    except Exception as e:
        print(e)

    try:
        age = Age(-5)
        print(age.get())
    except Exception as e:
        print(e)

    try:
        age = Age(500)
        print(age.get())
    except Exception as e:
        print(e)

    try:
        age = Age(25)
        print(age.get())
    except Exception as e:
        print(e)
        