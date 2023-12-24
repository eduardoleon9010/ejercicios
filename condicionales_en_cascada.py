# -*- coding: utf-8 -*-
def funcion_a()->None:
    print("Usted ha escogido la opcion a del menu")
    
def funcion_b()->None:
    print("Usted a escogido la opcion b del menu")
    
def funcion_c()->None:
    print("Usted ha escogido la opcion c del menu")
    
def funcion_d()->None:
    print("Usted ha escogido la opcion d del menu")
    
#PROGRAMA PRICIPAL

print("Menu principal")
print ("Opcion a")
print ("Opcion b")
print ("Opcion c")
print  ("Opcion d")

x = input("Seleccione su opcion: ")

if x == "a":
    funcion_a()
elif x == "b":
    funcion_b()
elif x == "c":
    funcion_c()
elif x == "d":
    funcion_d()

else:
    print("Seleccion invalida")
    
    
    