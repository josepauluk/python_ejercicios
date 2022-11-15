ventas_1=int(input('Ingrese las ventas del primer día: $'))
ventas_2=int(input('Ingrese las ventas del segundo día: $'))

if (ventas_1 > ventas_2):
    print('Las ventas del primer día fueron mayores de un total de: $', ventas_1)
elif (ventas_1 == ventas_2):
    print('Las ventas de los dos días es la misma, de monto: $', ventas_1)
else:
    print('Las ventas del segundo día fueron mayores de un total de: $', ventas_2)