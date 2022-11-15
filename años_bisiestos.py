#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
# Nota: para que un año sea bisiesto debe ser divisible por 4 y NO debe ser divisible por 100, excepto que sea también divisible por 400.


año1 = int(input('\nIngrese primer año: '))
año2 = int(input('Ingrese segundo año: '))


# for i in range(año1, año2):
#     if i % 10 == 0:
#         if i % 4 == 0:
#             if i % 100 != 0 or i % 400 == 0:
#                 print(f'{i} Es año bisiesto y múltiplo de 10')

#-----------------------------------------

# for i in range(año1, año2):
#     if not i % 10 == 0:
#         continue
#     if not i % 4 == 0:
#         continue
#     if i % 100 != 0 or i % 400 == 0:
#             print(f'{i} Es año bisiesto y múltiplo de 10')
    