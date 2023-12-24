# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:11:36 2022

@author: USUARIO
"""

def modificar(entero: int, cadena: str)->bool:
    entero += 100
    cadena += '!!!!'
    print(entero, cadena)
    return True
numero = 1
texto = "Hola Mundo"
resultado = modificar(numero, texto)
print(numero, texto)