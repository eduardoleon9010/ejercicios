# -*- coding: utf-8 -*-
def es_numero_primo(numero:int)->bool:
    primo = True
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
    
    return primo
