v = "\U0001F7E2"
b = "\U000026AA"
fila = int(input('Ingreser número de filas: '))
col = int(input('Ingreser número de columnas: '))

for f in range (fila):
    for c in range(col//2):
        if f % 2 == 0:
            print(v, end="")
            print(b, end="")
        else:
            print(v, end="")
            print(b, end="")
    
    if col % 2 != 0:
        if fila % 2 == 0:
            print(v, end="")
        else:
            print(b, end="")
    print()


# print(VERDE_CUADRADO)
# print(BLANCO_CUADRADO)



