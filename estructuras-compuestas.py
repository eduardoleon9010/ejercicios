# -*- coding: utf-8 -*-
def crear_figura(posicion: tuple, tamano: tuple)->dict:
    """ Crear una nueva fugura a  partir de los parametros recibidos

    Parameters
    ----------
    posicion  (tuple): una tupla con dos enteros que correspoden alas
                    coordenadas x y y de la esquina de la figura

    tamano  (tuple): una rupla con dos enteros que corresponen al ancho y
                    el alto de la figura

    Returns

    (dict): un diccionario que represnta la nueva figuray tiene
    las siguientes llaves: pos, tamanho, esquina, grosor, color_interno, 
    color_linea y rotacion.
    Para las ultimas 5 llaves de usan valores pedeterminados.
    """
    #Crear una nueva fugura con los valores de los parametros
    nueva_figura = {"pos": posicion, "tamanho": tamano}
    #Inicializar los otros atributos con valores por defecto
    nueva_figura["esquina"] = (0, 0)
    nueva_figura["grosor"] = 3
    nueva_figura["color_interno"] = None
    nueva_figura["color_linea"] = (0, 0, 0)
    nueva_figura["rotacion"] = (0, 0, 0)
    
    return nueva_figura


