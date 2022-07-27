# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 08:35:10 2022

@author: USER
"""

from turtle import*
color("red","yellow")
begin-fill()
while true:
    forward(145)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()    