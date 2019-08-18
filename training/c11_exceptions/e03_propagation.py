# Errors are propagared
def calc(num1, num2):
    return {'add': num1 + num2,
            'sub': num1 - num2,
            'mul': num1 * num2,
            'div': num1 / num2}

if __name__ == "__main__":
    try:
        num1 = int(input('Num1: '))
        num2 = int(input('Num2: '))

        result = calc(num1, num2)
        print('------ Results ------')
        print('ADD: ', result['add'])
        print('SUB: ', result['sub'])
        print('MUL: ', result['mul'])
        print('DIV: ', result['div'])
    except (ValueError, ZeroDivisionError):
        print('Invalid Input')
    except:
        print('Unknown Error')

    print('Program End')