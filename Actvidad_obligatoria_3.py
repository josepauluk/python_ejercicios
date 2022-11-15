numero=int(input('digame cuantas palabras tiene la lista: '))

if numero <1:
    print('imposible')
else:
    lista=[]
    for i in range(numero):
        print('digame la palabra', str(i+1)+': ', end='')
        palabra=input()
        lista+=[palabra]
    print('la lista creada es: ',lista)
