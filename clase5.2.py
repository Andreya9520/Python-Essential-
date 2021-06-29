#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:33:32 2021

@author: andreavergara
"""

"""
True cuando el codigo se ejecute un numero indefinido 
de veces
"""
x=input("Enter a number to count to: ")
x=int(x)
y=1
while True: 
    print(y)
    y=y+2#acumulador 
    if y>x:
        break 
while True:
    x=input("Enter a number to count to: ")
    if x=="q" or x== "quit": 
        break 
    x=int(x)
    y=1
    while True: 
        print(y)
        y=y+1
         if y>x: 
        break 