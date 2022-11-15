from Conjuntos_alumnos_funcion import *

primaria=set()
secundaria=set()
print('ALUMNOS DE PRIMARIA')
primaria=cargarNombre(primaria)
print('AUMNOS DE SECUNDARIA')
secundaria=cargarNombre(secundaria)

print('NOMBRE DE TODOS LOS ALUMNOS')
for nombre in primaria | secundaria:
    print(nombre)

print('NOMBRES COMUNES')
for nombre in primaria & secundaria:
    print(nombre)

print('NOMBRES DE PRIMARIA QUE NO ESTÁN SE REPITEN EN SECUNDARIA')
for nombre in primaria - secundaria:
    print(nombre)