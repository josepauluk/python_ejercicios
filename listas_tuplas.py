L=['almacenar',8,'a',[1,2,3],True,(0,0,1),85.7]
#Cuales de estos elementos pertenecen a la lista de arriba
lista_2=[85.7,0,True,[True],[(0,0,1)],85,'a',[1,2,3]]

# for lista_2 in L:
#     print(lista_2)

#Obtener posición en que se encuentra el elemento (0,0,1)
L.index((0,0,1))

#Cómo eliminar el último elemento de la lista
del L[len(L)-1]

#Utilizar una operación para contar cuántas veces aparece el string 'a'
L.count('a')