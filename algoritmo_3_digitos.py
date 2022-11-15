"""
Construya un algoritmo capáz de encontrar todas las cifras de tres dígitos
que cumplan con la condición de que la suma de los cubos de sus dígitos
sea igual al numero que la cifra representa.
Ejemplo:
1**3 + 5**3 + 3**3 = 1+125+27 = 153
"""

for i in range(100,1000):
    c = i // 100 #centena - división entera resultado '1'
    d = (i // 10) % 10 # decena - resultado '15' - resto con 10 da '5'
    u = i % 10 #unidad - cualquier número resto con 10 da el último número
    if (c**3 + d**3 + u**3) == i:
        print('Éste número cumple la condición: ',i)

print('-----------------------------------')

for i in range(100,1000):
    s = str(i) # convierte en string a la variable 'i' y la almacena en 's'
    suma = 0 # variable suma que comienza en cero para no estar dividiendo
    for x in s: #'s' es un string
        #print(x)
        suma = suma + int(x)**3
    if suma == i:
        print('Éste número cumple la condición: ',i)