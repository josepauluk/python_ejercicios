my_string = '''Este es un string que contiene \nsaltos de linea, \ncomo puedes ver,
Adios''' #Salto de línea

course = 'Python 3'
name = 'Jose'

final_messaje = 'Nueo curso de ' + course + ' por '  + name #1
final_messaje = 'Nuevo curso de %s por %s ' %(course, name) #2
final_messaje = 'nuevo curso de {} por {}' .format(course, name) #3
 #.format es un método que tienen las clases
#print(my_string)
print(final_messaje)