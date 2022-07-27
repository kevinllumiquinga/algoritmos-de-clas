# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:12:16 2022

@author: USER
"""
var1=int(input("ingrese la cantidad de tablas quieres imprimir"))

while var1>=1:
   
    suma=0
    promedio=0
   
    for j in range(1,var1):
        print("la tabla de N:",var1)
        par=0
        impar=0
        for i in range(1,16):
            res=i*j
            suma+=res
            promedio=suma//15
            print(i,"x",j,"=",res)
            if res%2==0:
                par=par+1
            else:
                impar=impar+1
        print("la suma de los numero es:",suma)
        print("el promedio de los numeros es: ",promedio)
        print("hay",par,"numeros pares")
        print("hay",impar,"numeros impares")
        print(" /n "*2)
        var5=int(input("si desea salir del programa digite (salir)"))
        if var5==0:
            break