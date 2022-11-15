#dni = int(input('Ingrese DNI: '))

def funcion(dni):
    long = len(dni)
    if long == 7 or long == 8:
        return True
    else:
        return False

#print(funcion(dni))