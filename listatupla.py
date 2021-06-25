#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:10:11 2021

@author: andreavergara
"""

hostenames=["R1", "R2", "R3", "R4"] 
lista1=["Juan",5,5.7,True, 5] 
print(type(lista1))
print(len(lista1))

tupla1=("Juan",5,5.7,False, 5)
print(type(tupla1))
print(len(tupla1))

print(lista1[0]," \n") 
print(lista1[1]," \n")
print(lista1[2]," \n")
print(lista1[-1]," \n")
print(lista1[-5]," \n")
print(tupla1[0]," \n")
print(tupla1[1]," \n")
print(tupla1[2]," \n")
print(tupla1[3]," \n")
print(tupla1[-1]," \n")
lista1[1]="CARLOS"
print(lista1) 

tupla1[0]="R2"
del lista1[2] #eliminar valores posición dentro de corchete 
del tupla1[0] #no se puede eliminar de la tupla 
