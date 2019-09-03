# data de prueba
text = 'hola!!!   abcd     ,    ..  de como   y  a 1   estas ?'

# separando las palabras por espacios
split_text = text.split(' ')
print(split_text)

quantity = 0
#for index in range(len(split_text)):
#    word = split_text[index]
for word in split_text:
    # elimina los espacios extras
    if(word != ''):
        # elimina los simbolos sobrantes (solitarios)
        if(word.upper() not in r'''1234567890,.;:[]{}/\!"#$%&/()='+-_^?¿¡|'''):
            quantity += 1
            print(word)

print(quantity)