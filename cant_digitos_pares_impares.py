

total_pares = 0
total_impares = 0
numero = int(input('\nIngrese un número: '))
while numero != 0:
    pares = 0
    impares = 0
    while numero != 0:
        ultimoDigito = numero % 10
        if ultimoDigito % 2 == 0:
            pares += 1
            total_pares += 1
        else:
            impares += 1 
            total_impares += 1
        numero = numero // 10 #elimina el último dígito
    print(f'El número tiene {pares} dígitos par/es y {impares} dígitos impar/es')
    numero = int(input('Ingrese un número: '))

print(f'Total dígitos pares:{total_pares}\nTotal dígitos impares:{total_impares}')