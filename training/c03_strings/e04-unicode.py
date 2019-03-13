# -*- coding: utf-8 -*-

texto = 'El niño está comiendo.'

print(texto)

texto = u'El niño está comiendo.'

print(texto)
print(texto.encode('utf-8'))
print(texto.encode('utf-8').decode('latin-1'))
