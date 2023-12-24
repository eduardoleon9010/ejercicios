# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:19:55 2022

@author: USUARIO
"""
#DataFrame a partir de diccionarios de listas
tiempos = [9.58, 9.69, 9.72, 9.74, 9.77]
atletas = ["Usain Bolt", "Usain Bolt","Usain Bolt","Asafa Powell","Asafa Powell"]
paises = ["Jamaica", "Jamaica","Jamaica","Jamaica","Jamaica"]
fechas = ["16/08/2009", "16/09/2008", "31/05/2008", "9/09/2007", "18/08/2006"]
cuidades = ["Berlin", "Beijing", "New York", "Rieti", "Zurich"]

datos = {"tiempo": tiempos, "atleta": atletas, "pais": paises, "fecha": fechas, "ciudad": cuidades}

df_records2 = pd.DataFrame(datos)