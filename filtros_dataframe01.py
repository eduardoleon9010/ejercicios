# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 19:02:30 2022

@author: USUARIO
"""

import pandas as pd
import math

peajes = pd.read_csv("peajes.csv", sep=";")

def calcular_peaje_cercano(peajes:pd.DataFrame)->None:
    distancias = []
    cercanos = []
    for i in range(peajes.shape[0]):
        actual = peajes.iloc[i]
        min_distancia = float('inf')
        mas_cerca =""
        for j in range(peajes.shape[0]):
            if i !=j:
                otro = peajes.iloc[j]
                dist = calcular_distancia_tierra(actual['latitud'],
                                                 actual['longitud'],
                                                 otro['latitud'],
                                                 otro['longitud'])
                if dist < min_distancia:
                    min_distancia = dist
                    mas_cerca = otro['NOMBRE']
                    
        distancias.append(min_distancia)
        cercanos.append(mas_cerca)
    print(len(cercanos))
    peajes['MAS_CERCANO'] = distancias
    peajes['DIST_MAS_CERCA'] = distancias
    
def calcular_distancia_tierra(t1:float, g1:float, t2:float, g2:float)->float:
    t1_rad = math.radians(t1)
    g1_rad = math.radians(g1)
    t2_rad = math.radians(t2)
    g2_rad = math.radians(g2)
    dist = 6371.01 * math.acos(math.sin(t1_rad) * math.sin(t2_rad) + math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad))
    return round(dist, 2)

calcular_peaje_cercano(peajes)
filtro = peajes[peajes['DEP'] == 'Cundinamarca']
print(filtro[['NOMBRE', 'MAS_CERCANO', 'DIST_MAS_CERCA']].iloc[5:10])




                
                