#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:42:40 2021

@author: andreavergara
Si no hay correcta identacion el codigo no se interpreta 
bien 
"""

while True:
    x=input("Enter a number to count to: ")
    if x=='q' or x== 'quit': 
        break 
    x=int(x)
    y=1
    while True: 
        print(y)
        y=y+1
        if y>x: 
            break 