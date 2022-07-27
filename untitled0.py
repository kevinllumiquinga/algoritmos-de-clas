# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:21:57 2022

@author: USER
"""

    
hora=int(input("ingrese una hora hh: "))
minutos=int(input("ingrese un valor en minutos: "))
segundos=int(input("ingrese una valor en segundos: "))
error=False
while hora>23 or hora <0 or minutos>59 or minutos<0 or segundos>59 or segundos<0:
    print("dato fuera de rango")
print("continuar")

if hora>23 or hora <0:
    print("dato de hora no es correcto")
    error=True
if minutos>59 or minutos<0:
    print("daro de minutos no es correcto")
    erro=True
if segundos>59 or segundos<0:
    print("daro de segundos no es correcto")
    error=True