# -*- coding: utf-8 -*-
def menor_posicion_lista(numeros:list)->int:
    indice = 0
    menor = numeros[0]
    
    for i in range(0, len(numeros)):
        if numeros[i] < menor:
            indice = i
            
    return indice

lista = [4,-1,-4,5,1,6,10,17,31,-14,-61]

print(menor_posicion_lista(lista))
