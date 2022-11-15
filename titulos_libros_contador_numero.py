"""titulo = input('\nIngrese título o "/" para fin de línea o "*" para finalizar\n>>> ')
lineas = 0
while titulo != '*':
    while titulo != '/':
        for i in titulo:
            digitos = 0
            if i in '0123456789':
                digitos += 1
            else:
                titulo = input('Ingrese título o '/' para fin de línea o '*' para finalizar')
    print(f'Línea completa. Aparecen {digitos} numéricos')
    lineas +=1
print(f'Fin. Se leyeron {lineas} completas')
#-----------Incompleto---------------------"""

digitosEnLaLinea = 0
cantLineas = 0
titulo = input('Titulo del libro: ')
while titulo != '*':
    if titulo == '/':
        cantLineas += 1
        print(f'Línea competa. Aparecen  {digitosEnLaLinea} dígitos.')
        digitosEnLaLinea = 0
    else:
        for caracter in titulo:
            if caracter in '0123456789':
                digitosEnLaLinea += 1
    titulo = input('Titulo del libro: ')
print(f'Fin. Se leyeron {cantLineas} líneas completas')
    

