"""# desafío 1
def degrada(item):
    'Determina los años de degradadión'
    material = {'bolsa': 150, 'botella': 1000, 'tetrabrik': 30, 'chicle': 5}
    return(material[item])

print(degrada('botella'),'años\n')"""


"""#Desafío 2
def relacion(a, b):
    'compara las toneladas recicladas de dos ciudades'
    if a > b:
        return 'Saenz Peña'
    elif a < b:
        return 'Quitilipi'
    else:
        return 'Saenz Peña y Quitilipi'

print(relacion(30,30))
"""

"""#Desafío 3
lista = {'saenz peña': 30, 'quitilipi': 101, 'bariloche': 300, 'neuquen': 150, 'cordoba': 35, 'resistencia': 3}
mas_de_100 = []
menos_de_100 = []

def separar(lista):
    'determina cuantas ciudades plantaron 100 o más plantas'
    cant = lista.values()
    cant = list(cant)
    for i in range (len(cant)):
        if cant[i] >= 100:
            mas_de_100.append(i)
        else:
            menos_de_100.append(i)
        return len(mas_de_100)

def cualesmas(mas_de_100):
    'dice las ciudades que cumplen con la condición >= 100'
    keys = (lista.keys())
    keys = list(keys)
    for i in mas_de_100:
        return keys[i]
print('Ciudades con 100 o más árboles plantados: (',separar(lista), ')', cualesmas(mas_de_100))

def cualesmenos(menos_de_100):
    'Dice las ciudades con menos de 100 áboles  plantados'
    keys = (lista.keys())
    keys = list(keys)
    for i in menos_de_100:
        return keys[i]
print('Las siudades con menos de 100 árboles palntados son: (',len(menos_de_100), ')', cualesmenos(menos_de_100))"""