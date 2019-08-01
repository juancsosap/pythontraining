palabra="ElGatoConBotasEstaDeViajePorElMundo"

resultado = ''
for letra in palabra:
 if (letra.isupper()):
  resultado += ',' + letra
 else:
  resultado += letra

if(resultado[0] == ','):
 resultado = resultado[1:]

print(resultado)   