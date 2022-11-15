N = int(input('Ingrese numero: '))
contador = 0
suma = 0

while contador <= N:
    suma = suma + contador
    contador += 1
    if contador == N * 0.5:
        print(' la suma está al 50%')

print(suma)

# sumatoria = 0
# for i in range(1, N+1):
#     sumatoria += i
#     if i == N * 0.5:
#         print('la sumatoria llegó al 50%:',sumatoria)
# print('Tota sumatoria:',sumatoria)

