"""frase = input('Ingresa una frase: ')
print('Vocales en la frase: ')
for x in 'aeiou':
    if x in frase: #'if nos dice si la vocal está en la frase y devueve True'
        print(x)
"""
frase = input('Ingresa una frase: ')
cantidad = 0
for x in frase:
    if x in 'aeiou': #'if nos dice si la vocal está en la frase y devueve True'
        cantidad +=1
print('Canidad de vocales', cantidad)