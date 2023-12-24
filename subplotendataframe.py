# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:06:20 2022

@author: USUARIO
"""

import pandas as pd
import matplotlib.pyplot as plt

peajes = pd.read_csv('peajes.csv', sep=";")
peajes['DEP'] = peajes['DEP'].replace(to_replace="<Null>",
                                      value='Otro')
peajes['DEP'] = peajes['DEP'].replace(to_replace="ANTIQUIA",
                                      value='Antioquia')
#Con subplots
tarifa_departamento = peajes[['DEP','CAT1', 'CAT2', 'CAT3', 'CAT4',
                              'CAT5', 'CAT6', 'CAT7',]]
grafica = tarifa_departamento.boxplot(by="DEP", rot=90, figsize=(10,6))

k = 1
for elemento in grafica:
    for i in elemento:
        i.set_title('Categoria '+str(k))
        i.set_xlabel('Departamento')
        i.set_ylabel('Tarifa en pesos')
        k+=1
        
plt.show()
         