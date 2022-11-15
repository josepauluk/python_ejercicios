preguntas=int(input('Ingrese cantidad de preguntas: '))
print('Total de preguntas >>>', preguntas)

correctas=int(input('ingrese cantidad de respuestas correctas: '))
print('total respuestas correctas >>>', correctas)

porcentaje = correctas * 100 / preguntas

# if(porcentaje >= 90):
#     print('Resultado fina EXCELENTE!')
# else:
#     if (porcentaje >= 70):
#         print('Resultado final BUENO!')
#     else:
#         if (porcentaje >= 60):
#             print('Resultado final APROBADO')
#         else:
#             print('No alcanzó!!!')

if (porcentaje >= 90):
    print('Resultado fina EXCELENTE!')
elif (porcentaje >= 70):
    print('Resultado final BUENO!')
elif (porcentaje >= 60):
    print('Resultado final APROBADO')
else:
    print('no aprobado!!!')