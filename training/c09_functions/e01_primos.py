numero = int(input("Numero: "))

'''
primo = True
if(num < 2):
    primo = False
else:
    for n in range(2, num):
        if(num % n == 0):
            primo = False
            break

if(primo):
    print("PRIMO")
else:
    print("NO PRIMO")
'''
import math

def isprimo(num):
    if(num < 2):
        return False
    else:
        for n in range(2, math.sqrt(num)):
            if(num % n == 0):
                return False
    return True


def primos(num):
    for n in range(2, num + 1):
        if(isprimo(n)):
            print(n, end='  ')


print("PRIMO" if isprimo(numero) else "NO PRIMO")
primos(numero)
