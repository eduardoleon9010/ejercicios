# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:39:31 2022

@author: USUARIO
"""

import pandas as pd

peajes = pd.read_csv("peajes.csv", sep=";")

# Peajes de Cundinamarca o Tolima
cundinamarca_tolima = peajes[(peajes['DEP'] == 'Cundinamarca') | (peajes['DEP'] =='Tolima')]
cundinamarca_tolima[['NOMBRE','DEP']]

#Peajes con tarifa de categoria 6 y 7 superiosr a 50000
peajes_cat6y7_costosa = peajes[(peajes['CAT6'] > 50000) & (peajes['CAT7'] > 50000)]
peajes_cat6y7_costosa[['NOMBRE', 'CAT6', 'CAT7']]

#Peajes de Atlantico o Valle de Cauca
valle_atlantico = peajes[peajes['DEP'].isin(['Atlántico','Valle del Cauca'])]
valle_atlantico[['NOMBRE','DEP']]





