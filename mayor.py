# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:59:42 2022

@author: USER
"""

import random 
while True:
     fil=int(input("ingrese el numero de filas: "))
     col=int(input("ingrese el numero de columnas: "))
     if fil>1 or fil<30 and col>1 or fil<30:
         print("continuar")
         break
     else:
        print("error se ingreso un valor fuera de rango")
        print("ingrese nuevamente los valor ")
        fil=int(input("ingrese el numero de filas:"))
        col=int(input("ingrese el numero de columnas:"))
        break
if fil>0 and col>0:
    matrix=[[int() for i in range(col)] for j in range(fil)]
    for filas in range(fil):
        for columnas in range(col):
            valor=random.sample(range(50,100),1 )
            matrix[filas][columnas]=valor
    for i in range(fil):
        print("/", end=" ")
        for j in range(col):
            print(matrix[i][j], "/", end=" ")
        print("")
    mayor=matrix[0][0]
    menor=matrix[0][0]
    for fi in matrix:
        for val in fi:
            if val > mayor:
                mayor = val
            if val<menor:
                menor= val
    print("el numero mayor dentro de la matriz es: ",mayor)