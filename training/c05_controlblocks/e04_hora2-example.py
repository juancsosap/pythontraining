hora = input("¿Que hora es? ")
hora = int(hora.replace(':', ''))

es_valida = hora >= 0 and hora < 2400
es_dia = hora > 600 and hora < 1800
print("dia" if es_dia else "noche" 
            if es_valida else "el valor debe estar entre 0 y 23")

print("Fin de programa.")
