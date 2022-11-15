import unittest
def titulo(cadena):
    nueva=""
    inicioPalabra=True              #indica el inicio de una palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False  #ya no es el inicio de una palabra 
            else:
                nueva=nueva+caracter.lower()
    return nueva

class Pruebas(unittest.TestCase):
    def tests_titulo(self):
        self.assertEqual(titulo('esto es una frase'), 'Esto Es Una Frase', 'Error convertir cadena a minúscula')
        self.assertEqual(titulo('ESTO ES UNA FRASE'), 'Esto Es Una Frase')
        self.assertEqual(titulo('palabra'), 'Palabra')
        self.assertEqual(titulo('   esto es una frase'), '   Esto Es Una Frase')
        self.assertEqual(titulo('esto es una frase   '),    'Esto Es Una Frase   ')
        self.assertEqual(titulo('esto   es   una   frase'),    'Esto   Es   Una   Frase')
        self.assertEqual(titulo(''),    '')
        self.assertEqual(titulo(' '),    ' ')
        self.assertEqual(titulo('123'),    '123')
        self.assertEqual(titulo('-1esto 2es 3una 4frase'),    '-1Esto 2Es 3Una 4Frase')
        self.assertEqual(titulo('esto1 es2 una3 frase4---'),    'Esto1 Es2 Una3 Frase4---')
        

if __name__ == "__main__":
    unittest.main()
