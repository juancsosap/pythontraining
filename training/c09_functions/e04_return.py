def isprime(num):
    if(num < 2):
        return False
    else:
        n = 2
        while n <= num**(1/2):
            if(num % n == 0):
                return False
            n += 1
    return True

def primes(num):
    return (n for n in range(2, num+1) if isprime(n))

def factorize(num):
    divisors = []
    while num > 1:
        factors = primes(num)
        for n in factors:
            if(num % n == 0):
                num //= n
                divisors.append(n)
                break;
    result = {}
    for n in divisors:
        result[n] = result.get(n, 0) + 1
    return result

def number(factors):
    result = 1
    for k, v in factors.items():
        result *= k**v
    return result

def decimal(fraction):
    return fraction[0] / fraction[1]

def simplify(fraction):
    num_factors = factorize(fraction[0])
    den_factors = factorize(fraction[1])
    factors = num_factors.copy()
    for f in factors:
        if f in den_factors:
            if num_factors[f] > den_factors[f]:
                num_factors[f] -= den_factors.pop(f)
            elif den_factors[f] > num_factors[f]:
                den_factors[f] -= num_factors.pop(f)
            else:
                num_factors.pop(f)
                den_factors.pop(f)
    num = number(num_factors)
    den = number(den_factors)
    return (num, den)

def split(fraction):
    intNum = fraction[0] // fraction[1]
    num = fraction[0] - intNum * fraction[1]
    return (intNum, (num, fraction[1]))

def fractionize(num):
    dotIndex = num.find('.')
    periodIndex = num.find('|') if num.find('|') > -1 else len(num)
    periodLen = (len(num) - periodIndex - 1) if periodIndex < len(num) else 0
    decLen = (periodIndex - dotIndex - 1) if dotIndex > -1 else 0
    intNum = int(num.replace('.', '').replace('|', '')) - \
             (int(num[:periodIndex].replace('.', '')) if periodLen > 0 else 0)
    intDen = int('1' + '0'*(decLen + periodLen)) - \
             (int('1' + '0'*decLen) if periodLen > 0 else 0)
    return simplify((intNum, intDen))

def abs(num):
    return num if num > 0 else -num

def aprox(num, dig):
    intNum = int(num)
    decNum = num - intNum
    result, nr, dr = 0, 0, 0
    gdelta, delta = num, -num
    n = 1
    for d in range(1, 10**dig):
        n = 1
        while(True):
            apr = n/d;
            delta = apr - decNum
            if(abs(delta) < gdelta):
                gdelta, nr, dr = abs(delta), n, d
            dif = int(abs(delta) * d)
            n += dif if dif > 0 else 1
            if(delta > 0): break;
    return (intNum, (nr, dr))

print(factorize(1234567890))

num = (25, 725)
print(num, decimal(num))
num = simplify(num)
print(num, decimal(num))

num = (24285120, 48570240)
print(num)
print(factorize(num[0]), factorize(num[1]))
num = simplify(num)
print(num)
print(factorize(num[0]), factorize(num[1]))

num = fractionize('12.55')
print(num, split(num), decimal(num))

num = fractionize('0.55')
print(num, split(num), decimal(num))

num = fractionize('.55')
print(num, split(num), decimal(num))

num = fractionize('55')
print(num, split(num), decimal(num))

num = fractionize('12.55|3')
print(num, split(num), decimal(num))

num = fractionize('12.55|33')
print(num, split(num), decimal(num))

num = fractionize('12.55|')
print(num, split(num), decimal(num))

num = fractionize('12.|3')
print(num, split(num), decimal(num))

num = fractionize('3.141592') # 3 17699/125000
print(num, split(num), decimal(num))
num = aprox(3.14159265358979323846, 4)
print(num, num[0] + num[1][0]/num[1][1]) # 3 16/113 -> 3.1415929203239825
num = aprox(3.14159265358979323846, 5)
print(num, num[0] + num[1][0]/num[1][1]) # 3 14093/99532 -> 3.1415926536189365
num = aprox(3.14159265358979323846, 6)
print(num, num[0] + num[1][0]/num[1][1]) # 3 140914/995207 -> 3.1415926535886505
num = aprox(3.14159265358979323846, 7)
print(num, num[0] + num[1][0]/num[1][1]) # 3 244252/1725033 -> 3.1415926535898153
