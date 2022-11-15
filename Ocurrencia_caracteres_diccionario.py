# cadena='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pulvinar ligula nibh, et convallis nulla rhoncus condimentum. Nulla mi tortor, aliquet ac nibh vel, vulputate accumsan lacus. Nulla a vulputate arcu. Nam blandit dignissim dui vitae vestibulum. Mauris scelerisque, augue vitae placerat suscipit, sem odio pulvinar leo, ut lobortis erat.'

contadores={}
alfabeto='abcdefghijklmnñiopqrstuvwxyz'
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(3):
    cadena=input('Cadena de caracteres: ')
    for caracter in cadena:
        if caracter.lower() in alfabeto:
            contadores[caracter]+=1
        # if caracter not in contadores.keys():
        #     contadores[caracter]=1
        # else:
        #     contadores[caracter]+=1
for caracter,cantidad in contadores.items():
    print(caracter, ':', cantidad)