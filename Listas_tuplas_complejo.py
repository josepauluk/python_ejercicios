#1- Solicitar al usuario que ingrese numeros, los cuales se guardarán en una lista. Finalizar al  ingresar en número 0, el cual no debe guardarse.
#2- A continuación, solicitar al usuario que ingrese números y, si el número está en la lista, elimnar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar(si no está en la lista).
#3- Imprimir la sumatoria de todos los numeros de la lista.
#4- Solicitar al usuario otro número y crea una lista con los elementos de a lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
#5- Genera e imprime una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la canidad de veces que aparece en ella. Por ejemplom si la lista original es [5,16,25,57,5,2] la nueva lista tendrá: [(5,3),(16,1)(2,2),(57,1)]

#1
list=int(input('\nIngrese número: '))
lista=[]
while list!=0:
    # if list==None:
    #     pass
    lista.append(list)
    list=int(input('Ingrese número: '))
print(lista)

#2
borrar=int(input('\nNúmero que se borrará si está en la lista: '))
if borrar in lista:
    lista.remove(borrar)
else:
    print('Ese numero no está en la lista')

#3
sumatoria=0
for i in lista:
    sumatoria+=i
print(f'\nLa sumatoria es: {sumatoria}')

#4
nro=int(input('\nFiltrar números menosres a: '))
nuevaLista=[]
for i in lista:
    if i <nro:
        nuevaLista.append(i)
for i in nuevaLista:
    print(i)

#5
print('Frecuencias')
nueva=[]
for n in lista:
    if (n, lista.count(n)) not in nueva:
        nueva.append((n, lista.count(n)))
#print(nueva)
for tupla in nueva:
    print(tupla[0], 'aparece', tupla[1], 'veces')
