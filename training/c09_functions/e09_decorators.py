import datetime

def logging(func):
    def inner(*args, **kwargs):
        value = func(*args, **kwargs)
        method = func.__name__
        time = datetime.datetime.now()
        msg = 'The method {} was called at {} returning the value {}\n'.format(method, time, value)
        with open('register.log', 'a') as file:
            file.write(msg)
        return value
    return inner

@logging
def add(n1, n2):
    return float(n1 + n2)

@logging
def sub(n1, n2):
    return float(n1 - n2)

@logging
def mul(n1, n2):
    return float(n1 * n2)

@logging
def div(n1, n2):
    return float(n1 / n2)

if __name__ == "__main__":
    num1 = int(input('NUM1: '))
    num2 = int(input('NUM2: '))
    oper = input('OPER: ')

    print('-'*15)

    print('RESU: ', end='')
    if(oper == 'A'): print(add(num1, num2))
    if(oper == 'S'): print(sub(num1, num2))
    if(oper == 'M'): print(mul(num1, num2))
    if(oper == 'D'): print(div(num1, num2))
    