# def mi_function(num1=0,num2=0):
#     print(num1 + num2)

# mi_function(4,7)

# def mi_function(cad,v=1): #cad = cadena, v = veces
#     print(cad * v)

# mi_function('Python\n',7)

# def mi_function(cad,v=1, **algomas): #*algomas : se convierte en tupla
#     print(cad * v)                  
#     for cadena in algomas:
#         print(cadena * v)

# mi_function('Python',7, 'Hola', 'Adiós', 'N', 'Cadenas')


# def mi_function(cad,v=1, **algomas): # **algomas :  se convierte en diccionario
#     print(cad * v)                  
#     print(algomas['cadenaExtra'])
#     print(algomas['cadenaDeMas'])

# mi_function('Python',7, cadenaExtra = 'Hola', cadenaDeMas = 'Adiós')

# def mi_function(num1, num2):
#     return num1 + num2

# resultado_de_suma = mi_function(3,4)
# print(resultado_de_suma)

# def saludar(persona = 'sin parametro'):
#     return 'Hola ' + persona

# print(saludar())


"""def calcular_volumen(alto, ancho = 1, profundidad = 1):
    return alto * ancho * profundidad
#resultado = calcular_volumen(2,6,9)
#print(resultado, 'cm3')
print(calcular_volumen(2,6,9), 'cm3')"""


"""def sumar(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sumar(2,3,6,7,6,3,33,435))"""


"""def saludar(*personas):
    for x in personas:
        print('Hola ' + x)

saludar('Sandra', 'Juan', 'Roberto')"""


"""# def config(**kwargs):
#       print(kwargs)

        #{'font': 'arial', 'color': 'red', 'size': '12'}

# config(font = 'arial', color = 'red', size = '12')

def config(**kwargs):
    for x in kwargs:
        print(x, ':', kwargs[x])
        #font : arial
        #color : red # Ésto imprime
        #size : 12

config(font = 'arial', color = 'red', size = '12')"""

#--------------------------------------

"""def funcion(a,b, *args, **kwargs):
    print('a:', a)
    print('b:', b)
    print(args)
    print(kwargs)

funcion(3,4,8,5,6,'f','r', color = 'red', size = '12')"""
# Resultado
# a: 3
# b: 4
# (8, 5, 6, 'f', 'r')
# {'color': 'red', 'size': '12'}
#--------------------------------------