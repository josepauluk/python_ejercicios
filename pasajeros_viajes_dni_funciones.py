def agregarPasajeros(pasajeros):
    '''Agrega pasajeros a la lista y retorna'''
    nombre=input('Nombre (x para cortar): ')
    while nombre !='x':
        dni=int(input('DNI: '))
        destino=input('Ciudad de destino:')
        pasajeros.append((nombre, dni, destino))
        nombre=input('Nombre (x para cortar): ')
    return pasajeros

def agregarCiudades(ciudades):
    '''Agrega ciudades a la lista y retorna'''
    ciudad=(input('Ciudad (x para cortar): '))
    while ciudad!='x':
        pais=input('Pais: ')
        ciudades.append((ciudad, pais))
        ciudad=(input('Ciudad (x para cortar): '))
    return ciudades


def buscarCiudad(pasajeros, dni):
    '''Dado el DNI de un pasajero, lo busca en la lista y retorna la ciudad a la que viaja. Si no se encuentra DNI retorna "" '''
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""


def cantidadPasajerosCiudad(pasajeros, ciudad):
    '''Dada una lista de pasajeros y una ciudad, retorna la cantidad de pasajeros que viajan a esa ciudad'''
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad


def buscarPaisDestino(pasajeros,ciudades, dni):
    '''Dada una lista de pasajeros, na de ciudad y un DNI, retorna el país al que viaja el pasajero con ese DNI'''
    ciudadBuscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==ciudadBuscada:
            return ciudad[1]
    return ""


def cantidadPasajerosPais(pasajeros, ciudades, pais):
    '''Dada una lista de pasajeros, una ciudad y un país, retorna la cantidad de pasajeros que viajan a ese país'''
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

# [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]
# [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]