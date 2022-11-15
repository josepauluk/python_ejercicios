#A lo largo de un curso se realizan dos exámenes parciales, 
# para aprobar el curso el promedio debe ser mayor o igual a 8 siempre y cuando en ambos 
# parciales se tenga al menos un 6. Escribir un programa que pregunte al usurio la nota de los
#dos parciales y muestre por pantalla si el alumno ha aprobado, o si no y en caso de no haber aprobado, que muestre
#que parcial debe repetir por tener una nota menor a 6

nota_1 = float(input('\nIngrese la primer nota: '))
nota_2 = float(input('Ingrese la segunda nota: '))

promedio = (nota_1 + nota_2) / 2

if nota_1 < 6:
    print('\nEl promedio es:', promedio,' Debe recuperar el primer parcial')
elif nota_2 < 6:
    print('\nEl promedio es:', promedio,' Debe recuperar el segundo parcial')
elif promedio < 8:
    print('\nEl promedio es:', promedio,' Aprobaste apenas!')
else:
    print('\nEl promedio es:', promedio, ' Felicitadiones Aprobaste')
