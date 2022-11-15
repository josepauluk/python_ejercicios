#https://www.youtube.com/watch?v=hF85etcCghY

"""
numero = 5 #5*4*3*2*1
factorial = 1 #inicia en '1'
while numero > 0:
    factorial = factorial * numero
    numero -=1
    print(factorial)
"""

"""
def factorial_numero():
    numero = 5 #5*4*3*2*1
    factorial = 1 #inicia en '1'
    while numero > 0:
        factorial = factorial * numero
        numero -=1
    print(factorial)

factorial_numero() #repetir función para no repetir código
factorial_numero() #repetir función para no repetir código
factorial_numero() #repetir función para no repetir código
"""

"""
def factorial_numero(numero): #reemplazamos numero por la variable numero
    #numero = 5 #5*4*3*2*1
    factorial = 1 #inicia en '1'
    while numero > 0:
        factorial = factorial * numero
        numero -=1
    print(factorial)

factorial_numero(4)
"""
def factorial_numero(numero):
    #numero = 5 #5*4*3*2*1
    factorial = 1 #inicia en '1'
    while numero > 0:
        factorial = factorial * numero
        numero -=1
    return factorial

resultado = factorial_numero(4)
print(resultado)

resultado = factorial_numero(5)
print(resultado)

resultado = factorial_numero(6)
print(resultado)
