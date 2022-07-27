# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:16:04 2022

@author: USER
"""

matrix=[[int() for i in range(2)] for j in range(2)]
for filas in range(2):
    for columnas in range(2):
        valor=int(input("ingrese el valor: "))
        matrix[filas][columnas]=valor
for i in range(2):
    print("/", end=" ")
    for j in range(2):
        print(matrix[i][j], "/", end=" ")
    print("")