""" MÉTODS DE FORMATO"""
course = 'Curso'
my_string = 'Código Facilito'

# Método 1
result = '{} de {}'.format(course, my_string)
print(result)

# Método 2
result = '{a} de {b}'.format(b=course, a=my_string)
print(result)

result = result.lower() #Curso de Código facilito
print(result)

result = result.upper() #Curso de Código facilito
print(result)

result = result.title() #Curso de Código facilito
print(result)


"""MÉTODOS DE BÚSQUEDA"""

pos = result.find('Facilito') #posición
count = result.count('o')
new_string = result.replace('o', 'x')
new_string_dos = result.split(' ')

print(pos)
print(result[7])
print(count)
print(new_string)
print(new_string_dos)