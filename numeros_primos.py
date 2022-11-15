# cantidad = 0
# n = int(input('\nIngrese número: '))
# while n != 0:
#     primo = True
#     for i in range(2, n):
#         if n % i == 0:
#             primo = False
#             break
#     if primo: # primo = True
#         cantidad += 1
#     n = int(input('Ingrese número: '))
# print('Primos: ', cantidad)

#---------------------------------------

numero = int(input('Número: '))
esPrimo = True
for i in range(2, numero):
    if numero % i == 0:
        esPrimo = False
        break
if esPrimo:
    print('Es número primo')
else:
    print('No es número primo')