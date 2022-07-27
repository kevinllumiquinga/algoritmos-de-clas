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
    print(hh,mm,ss)
else:
  print("fin de programa")# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

