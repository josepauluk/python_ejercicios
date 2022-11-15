sum_neg = 0
sum_pos = 0
cant_pos = 0
for i in range(6):
    nro = int(input(f'Ingrese número {i+1}: '))
    if nro >= 0:
        cant_pos += 1
        sum_pos += nro
    else:
        sum_neg += nro

print('\nSuma negativos: ', sum_neg)
if cant_pos != 0:
    print('Promedio positivos:', sum_pos/cant_pos)
else:
    print('No se ingresaron números positivos')