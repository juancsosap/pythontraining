edad = int(input("¿Cual es tu edad? "))

if(edad >= 18 and edad <= 70):
    print("mayor de edad")
    print("ya puedes entrar")
elif(edad > 70):
    print("ya estas muy viego")
    print("ya no puedes entrar")
else:
    print("menor de edad")
    print("no puedes entrar")

print("que vas a hacer?")
