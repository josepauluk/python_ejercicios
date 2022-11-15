frutas = {
    'Fresa':'roja',
    'Pera':'verde',
    'Papaya':'naranja',
    'Uva':'morada',
    'Guayaba':'rosa'
}

for valor in frutas: #frutas.value()
    print(f'{valor} es de color {frutas[valor]}') #{frutas['Fresa']}

for llave, valor in frutas.items(): #frutas.items() obtiene todos los valores
    print(f'{llave} es de color {valor}')