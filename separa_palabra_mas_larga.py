frase = input('Frase: ')
frase = frase.strip()
cantidad = 0
len_p_mas_larga = 0
while len(frase) != 0:
    cantidad +=1
    i = frase.find(" ") # i = índice del espacio / find() si no encuentra nada devuelve -1
    if i != -1:
        palabra = frase [0:i] #recorta la palabra desde el índice 0 hasta el indice i
        while i < len(frase) and frase[i] == " ":
            i = i + 1
        frase = frase[i:]
    else:
        palabra = frase
        frase = ""
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga = len(palabra)
        p_mas_larga = palabra
if cantidad > 0:
    print(f'Palabra más larga: {p_mas_larga}')
print(f'Cantidad de palabras: {cantidad}')