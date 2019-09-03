# Set Collection definition
cesta = {"pan", "vino", "queso", "carne", "pan"}
print(dir(set))

# Verify if a value is in a Collection
print(cesta)
print('fruta' in cesta) # >>>false
cesta.add('fruta')
print(cesta)
print('fruta' in cesta) # >>>false

# Extract element
print(cesta.pop())
print(cesta)

# Remove element
#cesta.remove('fruta') # The element must exist
print(cesta)
#cesta.discart('fruta') # Remove if exist

vinos = set()  # creación conjunto vacío

a = set('abracadabra')
print(a)
b = set('alacazam')
print(b)

# letras en a pero no en b {'r', 'b', 'd'}
print(a - b)

# letras en a o en b o en ambas {'a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'}
print(a | b)

# letras en a y en b {'a', 'c'}
print(a & b)

# letras en a o b pero no en ambos {'b', 'd', 'm', 'l', 'r', 'z'}
print(a ^ b)
