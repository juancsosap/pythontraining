hora = input("¿Que hora es? ")

if(not hora.isnumeric()):
    print("dato no valido")
else:
    hora_int = int(hora)
    if(hora_int >= 0 and hora_int < 24):
        if(hora_int > 6 and hora_int < 18):
            print("dia")
        else:
            print("noche")
    else:
        print("el valor debe estar entre 0 y 23")

print("Fin de programa.")
