# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:29:56 2022

@author: USUARIO
"""
import pandas as pd
import matplotlib.pyplot as plt

peajes = pd.read_csv('peajes.csv', sep=";")
peajes['DEP'] = peajes['DEP'].replace(to_replace="<Null>",
                                      value='Otro')
peajes['DEP'] = peajes['DEP'].replace(to_replace="ANTIQUIA",
                                      value='Antioquia')

#Boxplot sencillo
grafica = peajes[['DEP', 'CAT1']].boxplot(by="DEP", rot=90, figsize=(10,6))
plt.title('Tarifa Categoria 1 por Departamento')
plt.xlabel('DEPARTAMENTO')
plt.ylabel('Tarifa en pesos')
plt.show()

