from pasajeros_viajes_dni_funciones import *
pasajeros=[("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]
ciudades=[("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]
while True:
    print('1. Agregar pasajeros')
    print('2. Agregar ciudades')
    print('3. Buscar ciudad destino mediante el DNI')
    print('4. Cantidad de pasajeros que viajan a una ciudad')
    print('5. Busca país destino mediante DNI')
    print('6. Cantidad de pasajeros que viajan a un país')
    print('7. Salir del programa')
    opcion=int(input('Acción a ejecutar: '))
    if opcion==1:
        print('AGREGAR PASAJEROS')
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print('AGREGAR CIUDADES')
        ciudades=agregarCiudades(ciudades)
    elif opcion==3:
        dni=int(input('DNI: '))
        print('El pasajero viaja a', buscarCiudad(pasajeros, dni))
    elif opcion==4:
        ciudad=input('Ciudad: ')
        print('Viajan', cantidadPasajerosCiudad(pasajeros, ciudad), 'pasajeros')
    elif opcion==5:
        dni=int(input('DNI: '))
        print('Viaja a', buscarPaisDestino(pasajeros,ciudades, dni))
    elif opcion==6:
        pais=input('País: ')
        print('Viajan', cantidadPasajerosPais(pasajeros, ciudades, pais), 'pasajeros')
    elif opcion==7:
        break
    else:
        print('Opción no válida')