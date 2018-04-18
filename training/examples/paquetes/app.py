from vector_operations import suma, resta, multi, divi
from matrix_operations import sumaM, restaM, multiM, diviM


a1 = [1, 2, 3]
a2 = [4, 5, 6]

print(suma(a1, a2))
print(resta(a1, a2))
print(multi(a1, a2))
print(divi(a1, a2))

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 3, 5], [7, 9, 2], [4, 6, 8]]

print(sumaM(m1, m2))
print(restaM(m1, m2))
print(multiM(m1, m2))
print(diviM(m1, m2))
