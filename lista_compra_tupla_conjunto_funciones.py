def retornaDomicilios(lista):
    domicilios=set()
    for elemento in lista:
        domicilios.add(elemento[3])
        # for i in elemento[3]:
        #     domicilios.add(elemento[3])
    return domicilios