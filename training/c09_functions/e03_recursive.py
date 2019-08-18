def fact(num):
    return num * fact(num - 1) if num > 1 else 1;

def euler(num):
    return 1 / fact(num - 1) + euler(num - 1) if num > 0 else 0

def pi(num, ver = 1):
    r = 0
    if(ver == 1):
        while(num > 0):
            r += 6 / num**2
            num -= 1
        return r**(1/2)
    else:
        while(num >= 0):
            r += 4 * (-1)**num / (2*num + 1)
            num -= 1
        return r

print(euler(20))

print()

print(pi(1_000_000))
print(pi(1_000_000, 2))
