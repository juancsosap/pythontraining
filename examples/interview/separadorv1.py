texto = 'ElGatoConBotasSeFueDePaseo'

resultado = ''
for letra in texto:
    if(letra.isupper()):
        resultado += ',' + letra
    else:
        resultado += letra

if(resultado[0] == ','):
    resultado = resultado[1:]

print(resultado)
