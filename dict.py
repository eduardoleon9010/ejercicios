# -*- coding: utf-8 -*-

def avanzar_semestre(est1:dict,est2:dict,est3:dict,est4:dict)->None:
    est1['ssc'] += 1
    est2['ssc'] += 1
    est3['ssc'] += 1
    est4['ssc'] += 1
    
#PROGRAMA PRINCIPAL
e_1 = {'nombre':'Lina', 'codigo':'2020101234', 'genero':'femenino',
               'carrera':'Sistemas', 'promedio':4.78, 'ssc':4}
e_2 = {'nombre':'Laura', 'codigo':'2020105678', 'genero':'femenino',
               'carrera':'Civil', 'promedio':4.21, 'ssc':1}
e_3 = {'nombre':'Felipe', 'codigo':'2020109012', 'genero':'masculino',
               'carrera':'Sistemas', 'promedio':4.9, 'ssc':2}
e_4 = {'nombre':'Carlos', 'codigo':'2020103456', 'genero':'masculino',
               'carrera':'Economia', 'promedio':3.89, 'ssc':3}

print("Semestre estudiante 1:", e_1['ssc'])
print("Semestre estudiante 2:", e_2['ssc'])
print("Semestre estudiante 3:", e_3['ssc'])
print("Semestre estudiante 4:", e_4['ssc'])

avanzar_semestre(e_1,e_2,e_3,e_4)

print("Nuevo semestre estudiante 1:", e_1['ssc'])
print("Nuevo semestre estudiante 2:", e_2['ssc'])
print("Nuevo semestre estudiante 3:", e_3['ssc'])
print("Nuevo semestre estudiante 4:", e_4['ssc'])




