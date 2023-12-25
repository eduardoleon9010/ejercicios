"""
Este script en Python utiliza las librerías Pandas y Matplotlib para crear diagramas de caja 
 ("boxplots") para diferentes categorías de tarifas ('CAT1' a 'CAT7') según la columna 'DEP' 
(departamento) de un conjunto de datos leído desde un archivo CSV llamado 'peajes.csv'. 
El script lee los datos, realiza un preprocesamiento en la columna 'DEP' para reemplazar 
valores específicos, y genera un diagrama de caja para cada categoría de tarifa por departamento. 
La visualización resultante muestra la distribución de los valores de tarifas en los departamentos 
para cada categoría.
"""

import pandas as pd
import matplotlib.pyplot as plt

peajes = pd.read_csv('peajes.csv', sep=";")
peajes['DEP'] = peajes['DEP'].replace(to_replace="<Null>", value='Otro')
peajes['DEP'] = peajes['DEP'].replace(to_replace="ANTIQUIA", value='Antioquia')

# Con subplots
tarifa_departamento = peajes[['DEP', 'CAT1', 'CAT2', 'CAT3', 'CAT4',
                              'CAT5', 'CAT6', 'CAT7']]

grafica = tarifa_departamento.boxplot(by="DEP", rot=90, figsize=(10, 6))

k = 1
for elemento in grafica:
    for i in elemento:
        i.set_title('Categoría ' + str(k))
        i.set_xlabel('Departamento')
        i.set_ylabel('Tarifa en pesos')
        k += 1

plt.show()
