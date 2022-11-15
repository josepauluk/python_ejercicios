suma = 0
n = int(input('Número positivo: ')) # 23
while n != 0:
    digito = n % 10                 # se divide por 10 y el resto es "3" y se guarda en "digito" lugo se le suma el siguiente nro
    suma += digito                  # suma = 0 + digito = 3 == '3'
    n = n // 10                     # 23 // 10 = 2.3 se queda con "2" ahora "n" vale "2"
print('Suma de los dígitos:', suma)