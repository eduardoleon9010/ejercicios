# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:32:40 2022

@author: USUARIO
"""
#DataFrame partir de diccionarios de series 
tiempos = pd.Series([9.58, 9.69, 9.72, 9.74, 9.77])
atletas = pd.Series(["Usain Bolt", "Usain Bolt","Usain Bolt","Asafa Powell","Asafa Powell"])
paises = pd.Series(["Jamaica", "Jamaica","Jamaica","Jamaica","Jamaica"])
fechas = pd.Series(["16/08/2009", "16/09/2008", "31/05/2008", "9/09/2007", "18/08/2006"])
cuidades = pd.Series(["Berlin", "Beijing", "New York", "Rieti", "Zurich"])

datos_series = {"tiempo": tiempos, "atleta": atletas, "pais": paises, "fecha": fechas, "ciudad": cuidades}
df_records3 = pd.DataFrame(datos_series)