# -*- coding: utf-8 -*-
import random
def lanzar_dado(resultados: dict) -> None:
    """ Lanza un dado calculando aleatoriamente un número entre 1 y 6.
        Registra en el diccionario 'resultados' el valor que se obtuvo, asignándole
        el valor True a la llave que corresponde al valor.
    Parámetros:
      resultados (dict): Un diccionario que representa el conjunto de valores diferentes
                         que se han obtenido en los lanzamientos pasados.
    """
    valor = random.randint(1,6)
    resultados[valor] = True

# Lanzar el dado 6 veces y registrar los resultados obtenidos
def lanzar_6_dados()-> dict:
    """ Lanza el dado 6 veces y retorna un diccionario con los valores que se obtuvieron
    Resultado:
      (dict): Un diccionario donde sólo aparecen como llaves los valores que se
              obtuvieron en el lanzamiento del dado.
    """
    resultados = {}
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    return resultados

def contar_resultados_diferentes(resultados: dict) -> int:
    """ Cuenta cuántos resultados diferentes hubo
    Parámetros:
      resultados (dict): El conjunto de los resultados obtenidos representado
                         utilizando un diccionario. Si un valor aparece como
                         llave en el diccionario, significa que el valor se
                         obtuvo en el lanzamiento de los dados.
    Retorno:
      (int): La cantidad de resultados diferentes que hubo
    """
    diferentes = 0
    if 1 in resultados:
        diferentes += 1   
    if 2 in resultados:
        diferentes += 1
    if 3 in resultados:
        diferentes += 1
    if 4 in resultados:
        diferentes += 1
    if 5 in resultados:
        diferentes += 1
    if 6 in resultados:
        diferentes += 1
    return diferentes

# Lanzar el dado 6 veces y registrar los resultados obtenidos
resultados = lanzar_6_dados()
# Contar cuántos valores diferentes se obtuvieron
diferentes = contar_resultados_diferentes(resultados)
print("En 6 lanzamientos del dado se obtuvieron", diferentes, "valores diferentes")
