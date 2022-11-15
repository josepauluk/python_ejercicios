1#Calculadora de indice corporal (IMC)
print("Calculadora de indice corporal (IMC) \n")

contador = 0

while contador != 2:
    contador = int(input("¿Quieres seguir calculando el IMC? 1.Si 2.No \n"))

    if contador == 1:
        estatura = float(input("Ingrese su altura: "))
        peso = float(input("Ingrese su peso: "))
        resultado = round(peso/(estatura ** 2), 2)

        if resultado < 18.5:
            print(f"IMC {resultado} = BAJO PESO")
        elif 18.5 <= resultado < 25:
            print(f"IMC {resultado} = PESO NORMAL")
        elif 25 <= resultado < 30:
            print(f"IMC {resultado} = SOBREPESO")
        else:
            print(f"IMC {resultado} = OBESIDAD")

    elif contador == 2:
        print("Hasta pronto")

print("Gracias por usar la calculadora de IMC")

