# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:16:57 2022

@author: USUARIO
"""
import pandas as pd
import matplotlib.pyplot as plt

peajes = pd.read_csv('peajes.csv', sep=";")
peajes['DEP'] = peajes['DEP'].replace(to_replace="<Null>",
                                      value='Otro')
peajes['DEP'] = peajes['DEP'].replace(to_replace="ANTIQUIA",
                                      value='Antioquia')


#Multiplots
primera = peajes[peajes['DEP']=='Cundinamarca'].plot(kind='scatter',
                                                     x='CAT1',y='CAT2',
                                                     color='DarkBlue',label='1 a 2',
                                                     figsize=(0,6))
segunda = peajes[peajes['DEP']=='Cundinamarca'].plot(kind='scatter',x='CAT1',y='CAT3',
                                                     color='DarkGreen',label='1 a 3',
                                                     ax=primera, figsize=(10,6))

tercera = peajes[peajes['DEP']=='Cundinamarca'].plot(kind='scatter',x='CAT1',y='CAT4',
                                                     color='DarkRed',label='1 a 4',
                                                     ax=primera, figsize=(10,6))






