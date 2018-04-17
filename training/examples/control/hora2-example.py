hora = input("¿Que hora es? ")
hora = int(hora.replace(':', ''))

condi = hora > 600 and hora < 1800
print("dia" if condi else "noche")
