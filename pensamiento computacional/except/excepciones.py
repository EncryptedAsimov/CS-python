def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))


#como estructura de  control de flujo
def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return NoneS


### AFIRMACIONES ###
def primera_letra(lista_palabras):
    primeras_letras = []
    
    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es String'
            assert len(palabra) > 0 , 'No se permiten vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras


lista = ['Angelo',5.5, '', 2 , '43952353', 0.35]
print('Primeras letras validas son : ' , primera_letra(lista))



