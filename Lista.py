# -*- coding: utf-8 -*-
def promedio_lista(numeros:list)->float:
    sumatoria = 0
    total = 0
    
    for num in numeros:
        if num > 0:
            sumatoria += num
            total += 1
    promedio = sumatoria/total
    return promedio

lista = [4,-1,-4,5,1,6,10,17,31,-14,-61]          

print(promedio_lista(lista))

