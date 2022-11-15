from funcionSumaDigitos import *

cantidad=0
mayor=-1
numero=int(input('Número positivo: '))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma > mayor:
        mayor=suma
        n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input('Número positivo: '))
print(f'Sumatoria de dígitos de {n_mayorsuma}: {mayor}')
print(f'Cantidad con sumatoria menor  10: {cantidad}')