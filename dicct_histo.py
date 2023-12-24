# -*- coding: utf-8 -*-
def contar_vocales(texto: str) -> dict:
    """ Cuenta la cantidad de veces que aparece cada vocal dentro de un texto
    Parámetros:
      texto (str): El texto en el que van a contarse las vocales
    Retorno:
      (dict): Un diccionario donde las llaves son las vocales minúsculas y los valores
              son la cantidad de veces que aparece la vocal dentro del texto.
    """
    histograma = {}
    histograma['a'] = texto.lower().count('a')
    histograma['e'] = texto.lower().count('e')
    histograma['i'] = texto.lower().count('i')
    histograma['o'] = texto.lower().count('o')
    histograma['u'] = texto.lower().count('u')                
    return histograma

pangrama = 'Jovencillo emponzoñado de whisky, ¡qué figurota exhibe!'
vocales = contar_vocales(pangrama)
print(vocales)
