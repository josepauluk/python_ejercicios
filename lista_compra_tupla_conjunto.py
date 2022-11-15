from lista_compra_tupla_conjunto_funciones import *

lista=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
print('\tLista de clientes')
print('\n     NOMBRE     DÍA  MONTO   DOMICILIO')
for elemento in lista:
    print(elemento)
print('\nLas direcciones a las que se debe enviar las facturas son:')
domicilios=retornaDomicilios(lista)
for elemento in domicilios:
    print(elemento)

