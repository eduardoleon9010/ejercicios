# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:47:56 2022

@author: USUARIO
"""
import pandas as pd

peajes = pd.read_csv("peajes.csv", sep=";")

#Descriptivas
categoricas = peajes[['NOMBRE', 'CONCESION','GEN',
                      'SENTIDO', 'COD_VIA', 'DEP',
                      'CONCESIONA', 'INIC_OPER',
                     'ETIQUETA']]

numericas = peajes[['CAT1', 'CAT2', 'CAT3', 'CAT4',
                    'CAT5', 'CAT6', 'CAT7',]]

"""
categoricas.info()
numericas.info()

categoricas.describe()
numericas.describe()

categoricas['DEP'].unique()
categoricas['SENTIDO'].unique()
categoricas['GEN'].unique()
categoricas['DEP'].value_counts()

numericas.max()
numericas.idxmax()
categoricas[['NOMBRE', 'CONCESION', 'DEP']].loc[82]
"""







