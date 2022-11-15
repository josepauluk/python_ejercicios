#Ej2. Recorrer la siguiente lista [1,2,3,43,5,6,87] y parar cuando el valor 
# siguiente no sea el contiguo del anterior, es decir, luego del 3 viene el 4

# lista = [1,2,3,43,5,6,87]

# for item in lista:
#     print(item)
#     if item == 3:
#         break


lista= [1,2,3,45,5,6,87]
# item=0
# acum=1
# while acum==lista[item]:
#     print (lista[item])
#     acum+=1
#     item+=1
# print ("Fin del Programa")

contador = 1
for item in lista:
    print(item)
    if lista[contador] - item != 1:
        print(f"{lista[contador]} no es contiguo al {item}!!")
        break
    contador += 1


"""####WHILE
num=int(input("Ingrese un número:"+"\n" ))
total=0
acum=0
while acum<num:
    acum+=1
    total=total+acum
    print(total)
print("La suma final es", total)

#FOR
n= int(input("Ingrese un número: "))
resultado=0
acum=0
for i in range(1,n+1):
    acum+=1
    resultado=resultado+acum
    print(resultado)
print ("El resultado Final es:"+"\n",resultado)"""
