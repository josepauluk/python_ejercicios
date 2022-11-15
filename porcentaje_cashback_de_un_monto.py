#Retorna el porcentaje de un monto y un cashback ingresado.

monto = float(input('\nIngrese monto (0 ara terminar): '))

while monto > 0:
    cashback = float(input('Ingrese cashback: '))
    porciento = 0
    porciento = cashback * 100 / monto
    print(f'\nEl porcentaje de cashbak es de {round(porciento, 2)}%')
    monto = float(input('\nIngrese monto (0 ara terminar): '))
    