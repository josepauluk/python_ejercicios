# lista = [] # Fase
# for valor in range (0, 101):
#     lista.append(valor)
# print(lista)

lista = [ valor for valor in range (0, 101) ]
# print(lista)

# lista = [ 'x cosa' for valor in range (0, 101) ]
# print(lista)

# lista = [ valor for valor in range (0, 101) if valor % 2 == 0]
# print(lista)

tupla = tuple( ( valor for valor in range (0, 101) if valor % 2 != 0 ) )
#print(tupla)

diccionario = { indice:valor for indice, valor in enumerate(lista) if indice < 10 }
print(diccionario)

#1- valor a agregar a la lista
#2- un ciclo, for
#3- a la tupla solo se debe agregar la palabra 'tuple
#https://www.youtube.com/watch?v=Z-8Khdd2BUQ