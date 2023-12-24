# -*- coding: utf-8 -*-
def agregar_definicion_con_copia(diccionario: dict, palabra: str, definicion: str)-> dict:
  copia = diccionario.copy()
  copia[palabra] = definicion
  return copia

palabras = {'palabra1': 'definicion1', 'palabra2': 'definicion2'}
copia_palabras = agregar_definicion_con_copia(palabras, 'p99', 'def99')
palabras
{'palabra1': 'definicion1', 'palabra2': 'definicion2'}
copia_palabras
{'palabra1': 'definicion1', 'palabra2': 'definicion2', 'p99': 'def99'}