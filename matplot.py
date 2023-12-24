# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:21:39 2022

@author: USUARIO
"""

import random
import matplotlib.pyplot as plt
notas = []
ids_estudiantes = []
for i in range(30):
    nota_generada = random.normalvariate(3.25,0.98)
    nota_generada = round(nota_generada, 2)
    agregado = False
    while not agregado:
        id_generado = random.randint(20202001, 20202999)
        id_generado = str(id_generado)
        if id_generado not in ids_estudiantes:
            notas.append(nota_generada)
            ids_estudiantes.append(id_generado)
            agregado = True
            
plt.plot(ids_estudiantes, notas)
plt.title("Notas del curso")
plt.ylabel("Nota")
plt.xlabel("ID estudiante")
plt.xticks(rotation=90)
plt.show()

plt.hist(notas, bins=4, color=['green'], edgecolor='black', linewidth=1)
plt.title("Cantidad de estudiantes por rango de nota")
plt.ylabel("Cantidad de estudiantes")
plt.xlabel("Rango nota")
plt.show()

plt.scatter(ids_estudiantes, notas)
plt.title("Notas del curso")
plt.ylabel("Nota")
plt.xlabel("ID estudiante")
plt.xticks(rotation=90)
plt.show()
