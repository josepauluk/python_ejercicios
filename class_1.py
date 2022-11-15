# class Humano:
#     def __init__(self):
#         print('Soy un nuevo objeo')

# pedro = Humano()

# class Humano:
#     def __init__(self):
#         print('Soy un nuevo objeo')
    
#     def hablar(self, mensaje):
#         print(mensaje)

# pedro = Humano()
# raul = Humano()

# pedro.hablar('Hola')
# raul.hablar('Hola Pedro!')

# class Humano:
#     def __init__(self):
#         self.edad = 25
#         print('Soy un nuevo objeo')
    
#     def hablar(self, mensaje):
#         print(mensaje)

# pedro = Humano()
# raul = Humano()

# print('Soy Pedro y tengo: ', pedro.edad)
# print('Soy Raúl y tengo: ', raul.edad)
# pedro.hablar('Hola')
# raul.hablar('Hola Pedro!')

class Humano:
    def __init__(self, edad):
        self.edad = edad        
    
    def hablar(self, mensaje):
        print(mensaje)

pedro = Humano(26)
raul = Humano(21)

print('Soy Pedro y tengo: ', pedro.edad)
print('Soy Raúl y tengo: ', raul.edad)
pedro.hablar('Hola')
raul.hablar('Hola Pedro!')