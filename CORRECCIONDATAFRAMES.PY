# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:35:55 2022

@author: USUARIO
"""

import pandas as pd

peajes = pd.read_csv("peajes.csv", sep=";")

peajes.info()

peajes['COD_VIA'] = peajes['COD_VIA'].fillna('Sin Código ')
peajes['CAT4'] = peajes['CAT4'].fillna(0)
peajes['CAT5'] = peajes['CAT5'].fillna(0)

fechas_nulas = peajes[peajes['INIC_OPER'].isna()]
fechas_nulas[['NOMBRE','INIC_OPER','GEN']]
peajes['INIC_OPER'] = peajes['INIC_OPER'].fillna('01/01/2019')

peajes.info()

peajes['FECHA_INICIO_OP'] = pd.to_datetime(peajes['INIC_OPER'],
                                           infer_datetime_format=True,
                                           errors='coerce')

peajes.info()
peajes['FECHA_INICIO_OP'].head()

