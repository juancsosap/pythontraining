from functools import reduce

texto = 'ElGatoConBotasSeFueDePaseo'

resultado = reduce((lambda r, c: r + (',' if c.isupper() else '') + c), texto, '')
resultado = resultado[1:] if (resultado[0] == ',') else resultado

print(resultado)
