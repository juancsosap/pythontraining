def factorial(num):
    resultado = num
    for n in range(2, num):
        resultado = resultado * n
    return resultado

print(factorial(5))
print(factorial(7))
print(factorial(8))
print(factorial(9))

def sumador(lista):
    resultado = []
    size = len(lista)
    for i in range(size-1): # 0,1,2,3,4,5,.....,n-1
        resultado.append(lista[i] + lista[i+1])
    return resultado

def pascal(nivel):
    if(nivel == 0): return [1]
    if(nivel == 1): return [1, 1]
    else:
        prev_pascal = pascal(nivel - 1)
        result = sumador(prev_pascal) 
        result.append(1)
        result.insert(0, 1)
        return result

def pascal_pyramid(nivel, all=False):
    pyramid = []
    if(nivel >= 0): pyramid.append([1]) 
    if(nivel >= 1): pyramid.append([1, 1])
    if(nivel >= 2):
        for n in range(2, nivel + 1): # 2,3,4,5
            result_prev = pyramid[n-1] # [1, 1]  [1, 2, 1]   [1, 3, 3, 1]  [1, 4, 6, 4, 1]
            result = sumador(result_prev) # [2]  [3, 3]   [4, 6, 4]  [5, 10, 10, 5]
            result.append(1) # [2, 1]  [3, 3, 1]   [4, 6, 4, 1]  [5, 10, 10, 5, 1]
            result.insert(0, 1) # [1, 2, 1]   [1, 3, 3, 1]   [1, 4, 6, 4, 1]   [1, 5, 10, 10, 5, 1]
            pyramid.append(result)
    return pyramid if all else pyramid[-1]

print(pascal_pyramid(5))
print(pascal_pyramid(5, True))

print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
'''
r2 = sumador([1, 1])
r2.append(1)
r2.insert(0, 1)
print(r2)

r3 = sumador(r2)
r3.append(1)
r3.insert(0, 1)
print(r3)

r4 = sumador(r3)
r4.append(1)
r4.insert(0, 1)
print(r4)
'''
'''
0: 1
1: 1 1
2: 1 2 1
3: 1 3 3 1
4: 1 4 6 4 1
5: 1 5 10 10 5 1
6: 1 6 15 20 15 6 1
'''
#(var + sum)**pot

def poly(var, sum, pot):
    indices = pascal(pot)
    result = ''
    for i in range(pot+1):
        value = indices[i]*sum**i
        text = '*' + var + '^' + str(pot - i)
        termino = str(value) + text
        result += termino + (' + ' if i < pot else '')
    return result

result = poly('x', 5, 10) # (x + 5)**4
print(result) # "x**4 + 20*x**3 + 150*x**2 + 500*x + 625"    P[pot][pos]*sum**pos     pascal(4)[1]*5**1 + "*" + var + "**" + str(pot-1)









