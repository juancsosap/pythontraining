cesta = {"pan", "vino", "queso", "carne", "pan"}
print(cesta)

print('fruta' in cesta)  # >>>false

vinos = set()  # creación conjunto vacío

a = set('abracadabra')
b = set('alacazam')

# letras en a pero no en b {'r', 'b', 'd'}
print(a - b)

# letras en a o en b o en ambas {'a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'}
print(a | b)

# letras en a y en b {'a', 'c'}
print(a & b)

# letras en a o b pero no en ambos {'b', 'd', 'm', 'l', 'r', 'z'}
print(a ^ b)
