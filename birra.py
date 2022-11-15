print('\nFumamos un fasito hoy?')

while True:
    fasito = input('\ndale, decí que si (si/no): ')
    print('Dale vamos a fumar\n')
    if fasito == 'si':
        break
    elif fasito == 'no':
        continue
    else:
        print('Poné una respuesta válida!')
print('Traé el faso')
