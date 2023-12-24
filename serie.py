# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:12:50 2022

@author: USUARIO
"""

import pandas as pd

datos = [19, 18, 29, 14, 20, 20, 20, 20, 19]
fechas = ["5/11/20", "6/11/20", "7/11/20", "8/11/20", "9/11/20", "10/11/20",
          "11/11/20", "12/11/20", "13/11/20",]
temperaturas = pd.Series(datos, index=fechas, name="Temperaturas en Bogota")
