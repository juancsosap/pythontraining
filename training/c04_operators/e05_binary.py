num1 = 0b1011_1100
print('NUM1 {0:08b}'.format(num1))

num2 = 0b1100_1011
print('NUM2 {0:08b}'.format(num2))

print('    ----------')

num3 = num1 & num2
print('AND  {0:08b}'.format(num3))

num4 = num1 | num2
print('OR   {0:08b}'.format(num4))

num5 = num1 ^ num2
print('XOR  {0:08b}'.format(num5))

num6 = ~num1
print('NOT {0:08b}'.format(num6))

num7 = num1 >> 2
print('>>   {0:08b}'.format(num7))

num8 = num7 << 1
print('<<   {0:08b}'.format(num8))
