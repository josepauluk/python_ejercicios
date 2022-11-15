from funciones import *

nombre=input('\nNombre del socio: ')
while nombre!='':
    dni=int(input('DNI del socio: '))
    while not (DNIvalido(dni)):
        print('Número inválido')
        dni=int(input('DNI del socio: '))
    identificador=obtenerIdentificador(nombre,dni)
    print('El identificador del socio es: ', identificador)
    nombre=input('\nNombre del socio: ')