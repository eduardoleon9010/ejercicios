# -*- coding: utf-8 -*-

def contar_votos_estado(votos:list, estado_interes:str)->tuple:
    cant_votos_trump = 0
    cant_votos_biden = 0
    
    for voto_actual in votos:
       id_voto, candidato, estado, condado = voto_actual
       
       if estado == estado_interes:
           if candidato == "Donald Trump":
               cant_votos_trump += 1
           else:
               cant_votos_biden += 1
               
    return (cant_votos_trump, cant_votos_biden)

def contar_total_votos_por_estado(votos:list, estado:tuple)->dict:
    totales_estado = {}
    for i in range(len(estados)):
        estado_actual = estados[i]
        votos_estado_actual = contar_votos_estado(votos, estado_actual)
        totales_estado[estado_actual] = votos_estado_actual
        
    return totales_estado

import random
estados = ('Alaska','Alabama', 'Arkansas', 'Arizona', 'California',
           'Colorado', 'Connecticut', 'District of Columbia', 'Delaware',
           'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois',
           'Indiana', 'Kansas', 'Kentucky', 'Lousiana', 'Massachusetts',
           'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 
           'Mississippi', 'Montana', 'Nort Carolina', 'Nort Dackota',
           'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada'
           'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pensilvania',
           'Rhode Island', 'Soud Carolina', 'Sout Dakota', 
           'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington',
           'Wisconsin', 'West Virginia', 'Wyming')

votos = []
for est in estados:
    cant_votos = random.randint(4000, 8000)
    for i in range(cant_votos):
        elegido = random.randint(0,1)
        candidato = "Donald Trump"
        if elegido == 1:
            candidato = "Joe Biden"
        id_voto = est+str(i)
        voto = (id_voto, candidato, est, "Some Country")
        votos.append(voto)
        
cuenta = contar_total_votos_por_estado(votos, estados)
for estado in cuenta:
    print(estado, "\nTOTAL ->", "Trump: "+str(cuenta[estado][0]), 
          "Biden: "+str(cuenta[estado][1])+"\n")
        
        
        
        
        
        
        