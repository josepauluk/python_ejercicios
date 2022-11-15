number = int(input('Ingrese numero para calcular su factorial: '))
factorial = 1

if number != 0:
    for i in range (1,number+1):    
        factorial *= i        
print(f'El factorial de {number} es {factorial}')


