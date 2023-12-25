
"""
# Creación de un DataFrame desde Diccionarios de Series en Pandas
Este código utiliza Pandas, una biblioteca de Python para análisis de datos, para construir un DataFrame a 
partir de diccionarios que contienen series de datos. Cada serie representa una columna del DataFrame, y 
estas series se agrupan en un diccionario que organiza los datos relacionados con registros de atletismo, 
incluyendo información sobre tiempo, atleta, país, fecha y ciudad.
"""
import pandas as pd

# Series de datos individuales
tiempos = pd.Series([9.58, 9.69, 9.72, 9.74, 9.77])
atletas = pd.Series(["Usain Bolt", "Usain Bolt", "Usain Bolt", "Asafa Powell", "Asafa Powell"])
paises = pd.Series(["Jamaica", "Jamaica", "Jamaica", "Jamaica", "Jamaica"])
fechas = pd.Series(["16/08/2009", "16/09/2008", "31/05/2008", "9/09/2007", "18/08/2006"])
ciudades = pd.Series(["Berlin", "Beijing", "New York", "Rieti", "Zurich"])

# Creación del diccionario de series
datos_series = {
    "tiempo": tiempos,
    "atleta": atletas,
    "pais": paises,
    "fecha": fechas,
    "ciudad": ciudades
}

# Creación del DataFrame a partir del diccionario de series
df_records3 = pd.DataFrame(datos_series)

"""
Explicación:
Se definen cinco series (tiempos, atletas, paises, fechas y ciudades) utilizando la funcionalidad de 
Pandas para crear series a partir de listas.
Estas series se agrupan en un diccionario llamado datos_series, donde cada clave representa el nombre 
de una columna en el DataFrame y los valores son las series de datos correspondientes.
Se utiliza pd.DataFrame() para crear un nuevo DataFrame llamado df_records3 a partir del diccionario 
de series. Cada serie se convierte en una columna del DataFrame.
Este código puede ser útil para aquellos que ya tienen datos estructurados como series en Pandas y 
desean organizarlos en un DataFrame para su posterior análisis. Podrías complementar este ejemplo 
con técnicas de manipulación de datos, transformaciones o métodos para trabajar con series y DataFrames 
en Pandas en tu repositorio para proporcionar más contexto y utilidad a los usuarios.
"""


