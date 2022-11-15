"""
https://www.youtube.com/watch?v=7fBMgfbD570&list=PLb_E6BNMg5j7-MJ0ctjvKQlv2PU7qbMDb&index=20

Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.

Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.

Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.

"""
#----------------Encriptar--------------------------
corrimiento = int(input('Ingrese cantidad de lugares a correr: '))
alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

# for i in range(5):
#     msj = input('Ingrese msj 1: ')
#     msj_encriptado = ''
#     for caracter in msj:
#         if caracter.lower() in alfabeto:
#             posicion = alfabeto.find(caracter.lower()) #busca el índice
#             posicion = (posicion + corrimiento) % 27
#             msj_encriptado += alfabeto[posicion]
#         else:
#             msj_encriptado += caracter
#     print('***Mensaje encriptado:', msj_encriptado)

#------------------Desencriptar------------------------
for i in range(1):
    msj = input('Ingrese msj 1: ') #mtpf
    msj_encriptado = ''
    for caracter in msj:
        if caracter.lower() in alfabeto:
            posicion = alfabeto.find(caracter.lower()) #busca el índice
            posicion = (posicion - corrimiento) % 27
            msj_encriptado += alfabeto[posicion]
        else:
            msj_encriptado += caracter
    print('***Mensaje encriptado:', msj_encriptado)

