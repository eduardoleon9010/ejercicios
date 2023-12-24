# -*- coding: utf-8 -*-

def funcion(p1: str, p2: str, p3: dict, p4:dict) -> None:
    print("--> Valores recibidos:", p1, p2, p3, p4)
    print("--> Comparar las cadenas:", p1 == p2)
    print("--> Comparar los diccionarios:", p3 == p4, p3 is p4)
    
    p1 = "nueva cadena"
    p3["nuevo valor"] = 99
    print("--> Valores modificados:", p1, p2, p3, p4)
    p3 = {"ultimo": 1}
    print("--> Valores modificados de nuevo:", p3, p4)    
   
cadena = "cadena inicial"
diccionario = {"inicial": 0}

print("Antes de llamar a la función: ", cadena, diccionario)
funcion(cadena, cadena, diccionario, diccionario)
print("Después de llamar a la función: ", cadena, diccionario)

