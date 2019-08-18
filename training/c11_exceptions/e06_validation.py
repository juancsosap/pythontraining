def divisor1(num1, num2):
    if(num2 == 0):
        raise ArithmeticError('Calc Error')
    else:
        return num1 / num2

def divisor2(num1, num2):
    try:
        return num1 / num2
    except:
        raise ArithmeticError('Calc Error')

if __name__ == "__main__":
    try:
        num1 = int(input('Num1: '))
        num2 = int(input('Num2: '))

        print('DIV: ', divisor1(num1, num2))
        print('DIV: ', divisor2(num1, num2))
    except Exception as e:
        print('Error:', e)
