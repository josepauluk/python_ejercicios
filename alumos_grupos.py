"""Los alumnos de un curso se han dividito en dos grupos A y B de acuerdo al sexo y e nombre.
El grupo A está formado por las mujeres con el nombre anterior a la letra M y los hombres con la letra posterior a  la N.
Y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo correspondiente."""


sexo = input('Ingrese cual es el sexo, (F o M): ')
nombre = input('Ingrese cual es su nombre: ')

if sexo == 'F':
    if nombre.lower() < 'm':
        grupo = 'A'
    else:
        grupo = 'B'
else:
    if nombre.lower() > 'n':
        grupo = 'A'
    else:
        grupo = 'B'

print('\nUsted pertenece al grupo: ', grupo)