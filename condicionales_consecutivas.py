# -*- coding: utf-8 -*-
num1 = int (input("Digite un numero: "))
num2 = int (input("Digite un segundo numero: "))
num3 = int (input("Digite un tercer numero: "))

cuantos = 0

if (num1 % 2 == 0):
    cuantos += 1
if (num2 % 2 == 0):
    cuantos += 1
if (num3 % 2 == 0):
    cuantos += 1
print ("De los tres numeros digitados hay", cuantos, "pares" )



