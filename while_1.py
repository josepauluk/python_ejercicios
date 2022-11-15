contador = 0
bandera = True

while contador < 10: # < <= > >= == != 
    print(contador)
    contador +=1 # Aumenta el contador / contador = contador +1

    if contador  == 5:
        #print('estamos en el núero 5')
        continue
    if contador == 6:
        break
else:
    print('el contador a terminado')
    
while bandera:
    print(contador)
    contador +=1

    if contador == 6:
        bandera = False
else:
    print('El while a terminado')