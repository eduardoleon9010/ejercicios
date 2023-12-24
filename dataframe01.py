# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:00:18 2022

@author: USUARIO
"""
#Dataframe a paratir de diccionarios
a1 = {"tiempo": 9.58, "atleta": "Usain Bolt", "pais": "Jamaica", "fecha": "16/08/2009", "ciudad": "Berlin"}
a2 = {"tiempo": 9.69, "atleta": "Usain Bolt", "pais": "Jamaica", "fecha": "16/09/2008", "ciudad": "Beijing"}
a3 = {"tiempo": 9.72, "atleta": "Usain Bolt", "pais": "Jamaica", "fecha": "31/05/2008", "ciudad": "New York"}
a4 = {"tiempo": 9.74, "atleta": "Asafa Powell", "pais": "Jamaica", "fecha": "9/09/2007", "ciudad": "Rieti"}
a5 = {"tiempo": 9.77, "atleta": "Asafa Powell", "pais": "Jamaica", "fecha": "18/08/2006", "ciudad": "Zurich"}
records = [a1, a2, a3, a4, a5]

df_records1 = pd.DataFrame(records)