
def titulo(cadena):
    '''
    Recibe una cadena de caracteres y retorna una copia que tiene la
    primera letra de cada palabra en mayúsculas y el resto de las letras
    en minúsculas.
    >>> titulo('esto es una frase')
    'Esto Es Una Frase'
    >>> titulo('ESTO ES UNA FRASE')
    'Esto Es Una Frase'
    >>> titulo('palabra')
    'Palabra'
    >>> titulo('   esto es una frase')
    '   Esto Es Una Frase'
    >>> titulo('esto es una frase   ')
    'Esto Es Una Frase   '
    >>> titulo('esto   es   una   frase')
    'Esto   Es   Una   Frase'
    >>> titulo('')
    ''
    >>> titulo(' ')
    ' '
    >>> titulo('123')
    '123'
    >>> titulo('-1esto 2es 3una 4frase')
    '-1Esto 2Es 3Una 4Frase'
    >>> titulo('esto1 es2 una3 frase4---')
    'Esto1 Es2 Una3 Frase4---'
    '''
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
