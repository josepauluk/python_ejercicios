# print('Hola somos la pizería Bella Napoli.\nOfrecemos pizzas Vegetarianas y No Vegetarianas.\n')
# pizza=int(input('Tipee "1" para Vegetariana o "2" para No Vegetariana: '))

# if (pizza == 1):
#     print('Usted eligió una pizza Vegetariana')
#     vegg=int(input('Tipee "1" para Rúcula o "2" para Pimiento: '))
#     if(vegg == 1):
#         print('Usted eligió Vegetariana con Rúcula, mozzrella y tomate')
#     else:
#         print('Usted eligió Vegetariana con Pimiento, mozzrella y tomate')
# else:
#     print('Usted eligió una pizza No Vegetariana')
#     carr=int(input('Tipee "1" para Jamón o "2" para Panceta: '))
#     if(carr == 1):
#         print('Usted eligió No Vegetariana con Jamón, mozzrella y tomate')
#     else:
#         print('Usted eligió No Vegetariana con Panceta, mozzrella y tomate')

print('Bienvenido a la pizzería Bella Napoli.\nTipos de pizzas:\nTipo_1- Vegetariana\nTipo_2- No Vegetariana\n')
tipo = input('introduce el número correpondiente al tipo de pizza que quieres: ')

if tipo == "1":
    print('Ingredientes de pizzas vegetarianas\nTipo_1- Pimiento\nTipo_2- Rúcula\n')
    ingredientes = input('Introduce el ingrediente que deseas: ')
    print('Pizza vegetariana con mozzarella, tomate y ', end="")
    if ingredientes == "1":
        print('Pimiento')
    else:
        print('Rúcula')
else:
    print('\nIngredientes de pizzas no vegetarianas\nTipo_1- Jamón Crudo\nTipo_2- Jamón Cocido\nTipo_3- Panceta\n')
    ingredientes = input('Ingresa el número del ingrediente que deseas: ')
    print('Piza no vegetariana con mozzarella, tomate y ', end="")
    if ingredientes == "1":
        print('Jamón Crudo')
    elif ingredientes == "2":
        print('Jamón Cocido')
    else:
        print('Panceta')