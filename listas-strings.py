# -*- coding: utf-8 -*-

def insertar_ordenado(lista_ordenada: list, cadena: str) -> list:
    """
    Inserta una cadena de manera ordenada en una lista previamente ordenada.

    Parameters
    ----------
    lista_ordenada : list
        Lista ordenada en la que se insertará la cadena.
    cadena : str
        Cadena que se insertará en la lista.

    Returns
    -------
    list
        Lista resultante después de insertar la cadena.

    Notes
    -----
    Esta función inserta la cadena de manera ordenada en la lista proporcionada,
    manteniendo el orden ascendente de la lista.

    Examples
    --------
    lista_ordenada = ['apple', 'banana', 'orange']
    insertar_ordenado(lista_ordenada, 'kiwi')
    # Output: ['apple', 'banana', 'kiwi', 'orange']
    """

    i = 0

    # Encuentra la posición adecuada para la cadena
    while i < len(lista_ordenada) and cadena > lista_ordenada[i]:
        i += 1

    # Inserta la cadena en la posición encontrada
    lista_ordenada.insert(i, cadena)

    return lista_ordenada


# Uso de la función
lista = []

# Solicita al usuario ingresar cadenas hasta que ingrese 'terminar'
palabra = input("Ingrese una cadena, o 'terminar' para cerrar: ")

while palabra != 'terminar':
    insertar_ordenado(lista, palabra)
    palabra = input("Ingrese una cadena, o 'terminar' para cerrar: ")

print(lista)

