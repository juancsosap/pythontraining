print('Basic Calc'.center(40))
print(''.center(40,'-'))
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))

print(''.center(40,'-'))

print('Operations:')
print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Divition')
oper = input('Operation: ')

print(''.center(40,'-'))

if(oper in ('A', 'a','1')):
    print('Result: ', num1 + num2)
elif(oper in ('S', 's', '2')):
    print('Result: ', num1 - num2)
elif(oper in ('M', 'm', '3')):
    print('Result: ', num1 * num2)
elif(oper in ('D', 'd', '4')):
    print('Result: ', num1 / num2)
else:
    print('Invalid Operation')

print(''.center(40,'-'))
