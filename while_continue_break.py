frase = input('\nFrase: ')
l = input('Letra para buscar su posición: ')
i = 0
while i != len(frase):
    if l != frase[i]:
        print('No se encntró en la posición ', i)
        i += 1
        continue
    print('Se encontró en la posición ', i)
    break