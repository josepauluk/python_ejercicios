my_list = ['string', 15, 15.5, True]
my_list.append(6)
my_list.insert(1, 'insert')
my_list.remove(15)

print(my_list)
last_value = my_list.pop()
print(my_list[1])
print(last_value)

""" LISTA NÚMEROS ENTEROS"""

lista_numeros = [1,9,22,6,8,65,14,99]
lista_numeros_dos = [22,23]
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)
lista_numeros.sort(reverse=True)
print(lista_numeros)

lista_numeros.extend(lista_numeros_dos)
print(lista_numeros)

lista_numeros.append(lista_numeros_dos)
print(lista_numeros)