# [0,1,2,3,4,5,6,7,8,9]

num = 0
while(num < 10):
    print('{}^2 = {}'.format(num, num**2))
    num += 1

print()

for num in range(10):
    print('{}^2 = {}'.format(num, num**2))

print('-'*50)

num = 5
while(num < 10):
    print('{}^3 = {}'.format(num, num**3))
    num += 1

print()

for num in range(5, 10):
    print('{}^3 = {}'.format(num, num**3))

print('-'*50)

num = 2
while(num < 10):
    print('{}^4 = {}'.format(num, num**4))
    num += 3

print()

for num in range(2, 10, 3):
    print('{}^4 = {}'.format(num, num**4))
