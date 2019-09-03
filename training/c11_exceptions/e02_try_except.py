num1_str = input('Num1: ')
if not num1_str.isnumeric():
    print('Invalid Input')
else:
    num1 = int(num1_str)

    try:
        num2 = int(input('Num2: '))

        print('------ Results ------')
        print('ADD: ', num1 + num2)
        print('SUB: ', num1 - num2)
        print('MUL: ', num1 * num2)
        print('DIV: ', num1 / num2)
    except ValueError:
        print('Invalid Input')
    except ZeroDivisionError:
        print('Division by zero is not valid')
    except Exception as e:
        print('Unknown Error:', e)
    except: # the same as the previous except
        print('Unknown Error')

print('Program End')