lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
    pass #print(valor)

nuevo_rango = range(0,10,3)
for valor in nuevo_rango:
     pass #print(valor)

for valor in range(0,20,4):
    pass #print(valor)

# IGUAL AL POSTERIOR
indice = 0
for valor in lista:
    pass #print(valor, 'tiene el índice:', indice)
    indice +=1

# IGUA AL ANTERIOR
for indice, valor in enumerate(lista):
    pass #print(valor, 'tiene el índice:', indice)

#rint(len(lista))

for valor in range (0, len(lista)):
    pass #print(valor)

for valor in 'curso de código facilito':
    pass #print(valor)

diccionario = {'a': 100, 'b': 500, 'c': 20}
for llave,valor in diccionario.items(): # keys(), value()
    print('la llave', llave, 'tiene el valor de', valor)