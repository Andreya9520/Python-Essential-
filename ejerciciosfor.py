#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:54:46 2021

@author: andreavergara
"""

print("Comienzo")
for i in range(10,0,-1):
    print(i, end=" ")
print()
print("Final")


veces = int(input("¿Cuántas veces quiere que le salude? "))
for i in range(1,veces+1,1):
    print("Hola ", end="")
print()
print("Adiós")

lista1=["R1","R2","R2"]
for i in range(0,len(lista1)):
    print(i)
# 0
# 1
# 2