"""
Un local vende remeras por mayor y  menor

si la compra es mayor  o igual a 10 remeras
el precio es del 80%

preguntar la cantidad de remeras que va a comprar
y ell precio por unidad

devolver el total de la compra
"""
        #Condicional simple
        
precio = float(input('Ingese precio por unidad: $'))
unidades = int(input('Ingrese cantidad de remeras: '))

if unidades >= 10:
    total = unidades * precio * 0.8
else:
    total = unidades * precio

print('El total de la compra es de: $', total)