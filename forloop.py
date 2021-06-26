#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:52:34 2021

@author: andreavergara
"""

"""
FOR LOOP
su aplicacion es utilizarlo para leer cadena de caracteres
numero determinado de veces en alguna condicion 
las listas son silimares a los vectores con otro nombre. 
"""
devices= ["R1", "R2", "R3", "S1", "S2"]
for item in devices: 
    print (item)

lista=["R1", "R2", "R3",
       "S1","S2","AP"]
print(len(lista))
print ("antes de for")

for a in lista :
    print (a)
    print("dentro de for")
print ("fuera de for")

