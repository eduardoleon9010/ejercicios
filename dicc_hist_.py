# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:03:11 2024

@author: USUARIO
"""

def construir_histograma(valores: list) -> dict:
    """
    Construye un histograma a partir de una lista de valores.

    Parámetros:
    - valores (list): La lista de valores para la cual se construirá el histograma.

    Retorna:
    - dict: Un diccionario donde las llaves son los valores únicos y los valores son
            la cantidad de veces que aparece cada valor en la lista.
    """
    histograma = {}
    for valor in valores:
        if valor in histograma:
            histograma[valor] += 1
        else:
            histograma[valor] = 1
    return histograma

# Ejemplo de uso
valores_ejemplo = [1, 2, 3, 2, 1, 3, 4, 1, 2, 4, 5]
histograma_resultante = construir_histograma(valores_ejemplo)
print("Histograma Resultante:", histograma_resultante)
