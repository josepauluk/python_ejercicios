# -Ej3. Imprimir por pantalla 10 veces el string "-" con la cantidad de guiones 
# representando la iteracion en la que se encuentra, por ejemplo, iteracion 1 "-", 
# iteracion 5 "-----".


# for i in range(1,11):
#     print(i*"-")
# print ("Final")

for x in range(1,11):
    guion = "-"
    print(f'Iteracion {x} "{guion*x}"')