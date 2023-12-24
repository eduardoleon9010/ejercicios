# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:55:21 2022

@author: USUARIO
"""

def comparar_tiempos(tiempo_1:str, tiempo_2:str)->int:
    partes_1 = tiempo_1.split(":")
    partes_2 = tiempo_2.split(":")
    
    hora_1 = int(partes_1[0])
    minutos_1 = int(partes_1[1])
    segundos_1 = int(partes_1[2])
    
    hora_2= int(partes_2[0])
    minutos_2 = int(partes_2[1])
    segundos_2 = int(partes_2[2])
    
    comparar = 0
    
    if hora_1 > hora_2:
        comparar = 1
    elif hora_1 < hora_2:
        comparar = -1
    else:
        if minutos_1 > minutos_2:
            comparar = 1
        elif minutos_1 < minutos_2:
            comparar = -1
        else:
            if segundos_1 > segundos_2:
                comparar = 1
            elif segundos_1 < segundos_2:
                comparar -1
    
    return comparar

def vuelo_llega_mas_tarde(vuelos:list)->dict:
    llegadas = hora_llegada_vuelos(vuelos)
    
    pos_mas_tarde = 0
    llegada_mas_tarde = llegadas[0]['tiempo_llegada']
    
    for i in range(0, len(llegadas)):
        tiempo = llegadas[i]['tiempo_llegada']
        
        if comparar_tiempos(tiempo, llegada_mas_tarde) == 1:
            pos_mas_tarde = i
            llegada_mas_tarde = tiempo
            
    return vuelos[pos_mas_tarde]


vuelos = [{'tiempo_salida':'08:11:45','duracion':'2:54:20'},
          {'tiempo_salida':'11:48:10','duracion':'2:11:58'},
          {'tiempo_salida':'12:00:10','duracion':'0:50:15'},
          {'tiempo_salida':'14:55:10','duracion':'3:20:00'},
          {'tiempo_salida':'17:15:20','duracion':'4:05:11'}]

print(vuelo_llega_mas_tarde(vuelos))
    


    
    
    
    
    


    