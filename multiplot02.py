# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:28:31 2022

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
quinta = peajes[peajes['DEP']=='Cundinamarca'].plot(kind='scatter',x='CAT1',y='CAT2',
                                                     c='CAT3',s=peajes['CAT4']/100,
                                                     figsize=(10,6))

plt.show()