# -*- coding: utf-8 -*-
def insertar_ordenado(lista_ordenada:list, cadena:str)->list:
    i = 0
    
    while i < len(lista_ordenada) and cadena > lista_ordenada[i]:
        i+=1
        
    lista_ordenada.insert(i,cadena)
    
    return lista_ordenada

def ordenar_lista(lista_desordenada:list)->list:
    ordenada = []
    
    for cadena in lista_desordenada:
        ordenada = insertar_ordenado(ordenada, cadena)
        
    return ordenada

lista = ["tanque", "avion", "moto", "automovil", "barco", "diligencia"]

orden = ordenar_lista(lista)

print(orden)
