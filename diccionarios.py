# Las claves deben ser inmutables
# Si existen claves iguales toma el valor de la última
# Pueden crecer y decrecer
#             llave/clave valor 
diccionario = { 'a': 55, 'a': True, 5: 'esto es un string', (1,2): False }
diccionario['c'] = 'nuevo string' #crear clave/valor
diccionario['a'] = False #si se encuentra misma llave/clave se actualiza sinó crea

#valor = diccionario['a'] #obtenemos los valores
valor = diccionario.get(5, 'nose') #si no encuentra el valor regresa lo siguiente
#del diccionario[5]
#print(diccionario)
#print(valor)

#llaves = diccionario.keys() #objeto iterable
llaves = list(diccionario.keys()) #objeto iterable
#valores = diccionario.values()
valores = list(diccionario.values())

llaves = tuple(diccionario.keys()) 
valores = tuple(diccionario.values())

diccionario_dos = {'z': 23, 'w': 88}
#diccionario['z'] = diccionario_dos['z']
#diccionario['w'] = diccionario_dos['w']

diccionario.update(diccionario_dos) #agrega el diccionario_ dos a diccionario

#print(llaves)
print(valores)
print(diccionario)