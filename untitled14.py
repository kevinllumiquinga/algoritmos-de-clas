# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:23:24 2022

@author: USER
"""

def fibonacci_iter(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0',end=(" "))
        print(a,end=(" "))
        print(b,end=(" "))
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total,end=(" "))
var1=(int(input("ingrese un valor")))       
fibonacci_iter(var1-1)
