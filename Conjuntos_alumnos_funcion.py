def cargarNombre(alumnos):
    nombre=input('Nombre: ')
    while nombre !='x':
        alumnos.add(nombre)
        nombre=input('Nombre: ')
    return alumnos