while(True):
    hora = input("¿Que hora es? ")

    if(hora.isnumeric()):
        hora_int = int(hora)
        if(hora_int >= 0 and hora_int < 24):
            break

    print("dato no valido")

condi = hora_int > 6 and hora_int < 18
print("dia" if condi else "noche")