"""monto = float(input('Ingrese monto de artículo (0 para terminar): $'))
suma = 0

while monto != 0:
    while monto < 0:
        monto = float(input('Ingrese monto positivo!! (0 para terminar): $'))
    suma += monto
    monto = float(input('Ingrese nuevo monto (0 para terminar): $'))
print('Sub Total: $',suma)
if suma >= 1000:
    total = suma - (suma * 10 / 100)
    print(f'Total a pagar ${total}\ncon un descuento del 10% por superar compra mayor a $1000')
else:
    print(f'Total a pagar ${suma}\nsin descuento por compra inferior a $1000')
"""
#-----------------------------------------------------
total = 0
monto = float(input('Monto de venta: $'))
while monto != 0:
    if monto < 0:
        print('Monto no valido!')
    else:
        total += monto
    monto = float(input('Monto de venta: $'))
if total > 1000:
    total -= total * 0.1 #-10% tota = total - (total * 0.1)
print('Monto total a pagar: $', total)