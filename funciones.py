def DNIvalido(dni):
    'valida un DNI'
    cantidad=0
    while dni!=0:
        cantidad+=1
        dni=dni//10
    return cantidad==7 or cantidad==8

def factorial(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -=1
    return factorial

def lenUltmaPalabra(cadena):
    longitud=len(cadena)
    if longitud==0:
        return 0
    cantidad=0
    for i in range(longitud):
        if cadena[i]!=' ':
            cantidad+=1
        else:
            if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
                cantidad=0
    return cantidad

def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primerosTresDigitos(numero):
    'Quita los ultimos números hasta que solo queden 3 y al resultado lo convierte en entero para aiminar los decimales'
    while numero>=1000:
        numero=numero/10
    return int(numero)


def obtenerIdentificador(nombre,dni):
    nombre=nombre.strip()
    i=nombre[0:nombre.find(' ')]
    i=i+str(lenUltmaPalabra(nombre))
    i=i+str(primerosTresDigitos(dni))
    return i
