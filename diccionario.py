# -*- coding: utf-8 -*-
palabras = { 'imagen' : 'Figura, representación, semejanza y apariencia de algo',
             'figura' : 'Forma exterior de alguien o de algo', 
             'baraja' : 'Conjunto completo de cartas empleado para juegos de azar',
             'posibilidad' : 'Aptitud, potencia u ocasión para ser o existir algo' }

definicion_imagen = palabras['imagen']
print(definicion_imagen)


definicion_figura = palabras['figura']
print(definicion_figura)

llave = 'IMAGEN'
# Preguntar si la llave está en el diccionario antes de consultar
if llave in palabras:
  definicion = palabras[llave]
else:
  definicion = "La palabra '" + llave + "' no se encuentra en el diccionario"