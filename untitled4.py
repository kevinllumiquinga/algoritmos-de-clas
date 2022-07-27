# -*- coding: utf-8 -*-
"""
Created on Thu May 26 22:43:56 2022

@author: USER
"""
hora=int(input("ingrese una hora hh: "))
minutos=int(input("ingrese un valor en minutos: "))
segundos=int(input("ingrese una valor en segundos: "))
error=False
if hora>23 or hora <0:
  print("dato de hora no es correcto")
  error=True
if minutos>59 or minutos<0:
  print("daro de minutos no es correcto")
  erro=True
if segundos>59 or segundos<0:
  print("daro de segundos no es correcto")
  error=True

if error==False:
  print("puede continuar")
  nuevo=int(input("ingrese el valor de los segundos extra: "))
  if nuevo<0:
    print("el valor de los segundos extra son invalidos")
  else:
    print("puede continuar")
    segundosn=(hora*3600)+(minutos*60)+segundos
    suma=nuevo+segundosn
    hh=int(suma/3600)
    mm=int((suma/60)-(hh*60))
    ss=int((suma-(mm*60)-(hh*3600)))
    if hh>10:
        hh2=print("0",hh)
    elif hh<10:
         hh2=print(hh)
    if mm>10:
         mm2=print("0",mm)
    elif mm<10:
         mm2=print(mm)
    if ss>10:
         ss2=print("0",ss)
    elif ss<10:
         ss2=print(ss)

print(hh2,":",mm2,":",ss2,end=())