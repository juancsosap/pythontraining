def inrange(num, min, max):
    if(not (num >= min and num <= max)):
        raise ValueError

def getnum(msg, zeroable=True):
    while(True):
        try:
            num = int(input(msg))
            inrange(num, 0, 100)
            if(not zeroable): 1/num
            break
        except:
            print('Invalid Input')
    return num

num1 = getnum('Num1: ')
num2 = getnum('Num2: ', False)

try:
    print('------ Results ------')
    print('ADD: ', num1 + num2)
    print('SUB: ', num1 - num2)
    print('MUL: ', num1 * num2)
    print('DIV: ', num1 / num2)
except Exception as e:
    print('Error:', e)

print('Program End')