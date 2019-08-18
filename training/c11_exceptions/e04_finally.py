# Errors are handled
def calc(num1, num2, oper):
    try:
        if oper == 'add': return num1 + num2
        elif oper == 'sub': return num1 - num2
        elif oper == 'mul': return num1 * num2
        elif oper == 'div': return num1 / num2
        else: return None
    except:
        print('Error Generated')
    finally:
        print('Calc Method Called')
    
if __name__ == "__main__":
    try:
        num1 = int(input('Num1: '))
        num2 = int(input('Num2: '))

        print('------ Results ------')
        print('ADD: ', calc(num1, num2, 'add'))
        print('SUB: ', calc(num1, num2, 'sub'))
        print('MUL: ', calc(num1, num2, 'mul'))
        print('DIV: ', calc(num1, num2, 'div'))
    except ValueError:
        print('Invalid Input')
    except:
        print('Unknown Error')

    print('Program End')