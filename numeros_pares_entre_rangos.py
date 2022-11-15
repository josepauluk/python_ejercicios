print('Mostrar la suma y la cantidad de números pares comprendidos entre dos números ingresados por teclado')

primer_numero = int(input('Ingrese el primer número: '))
segundo_numero = int(input('Ingrese el segundo número: '))

cantidad = 0

while primer_numero < segundo_numero:
    if primer_numero % 2 == 0:
        print(primer_numero)
        cantidad += 1
    primer_numero += 1
print('hay', cantidad, 'números pares')