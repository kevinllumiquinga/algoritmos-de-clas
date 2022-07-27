# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:16:34 2022

@author: USER
"""

def factorial(n):
    if n==0 or n==1:
        resultado=1
        print(resultado)
    elif n>1:
        resultado=n+factorial(n-1)
        print(resultado)
    return resultado

var1=int(input("ibgrese el numero que desea sacar el factorial: "))
ress=factorial(var1)
print(ress)






