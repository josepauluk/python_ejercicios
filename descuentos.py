
importe = float(input('\nIngrese monto a cobrar: $'))
print('\nPorcentajes de desuentos:\nMás de $15.000 50%.\nMás de $10.000 30%.\nMás de $5.000 20%.\nMás de $3.000 10%\n')


if importe >= 15000:
    print('El descuento es del 50%')
    total = importe * 0.5
    print('El importe a pagar con descuento sería de: $',importe-total)
elif importe >= 10000:
    print('El descuento es del 30%')
    total = importe * 0.3
    print('El importe a pagar con descuento sería de: $',importe-total)
elif importe >= 5000:
    print('El descuento es del 20%')
    total = importe * 0.2
    print('El importe a pagar con descuento sería de: $',importe-total)
elif importe >= 3000:
    print('El descuento es del 10%')
    total = importe * 0.1
    print('El importe a pagar con descuento sería de: $',importe-total)
else:
    print('No tiene descuento. Importe a pagar: $',importe)