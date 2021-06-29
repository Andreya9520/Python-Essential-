#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:17:57 2021

@author: andreavergara
"""

def mensaje ():
    print ("\tPor favor ingresa el numero: \n")

print ("Inicio")
mensaje()
a=input()
mensaje()
b=input()
mensaje()
c=input()
print(a,b,c)

def hi (name): 
    print ("Hi: ",name)
hi ("Juan Carlos")
hi("cec")
hi("Ana")

"""
Created on Mon Jun 28 20:30:00 2021

@author: andreavergara
arg es un argumento para convertir en una tupla, me permite 
hacer que la funcion se convierta en distintos valores

"""

def suma(*arg):
    print("Tipo de datos del argumento; ", type(arg))
    sum = 0
    
    for n in arg: 
        sum +=n 
        #sum=sum+n 
        
    print ("Suma: ", sum)
    
suma(3)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,5,6)

"""
Created on Mon Jun 28 20:36:54 2021

@author: andreavergara
"""

def keyw(**datos):
    print("\nTipo de datos del argumento:",type(datos))

    for key, value in datos.items():
        print("{} is {}".format(key,value))

keyw(Firstname="Juan", 
     Lastname="Domínguez", 
     Age=42, 
     Phone=1234567890)
keyw(Firstname="John", 
     Lastname="Wood",
     Email="johnwood@nomail.com",
     Country="Wakanda", 
     Age=25, 
     Phone=9876543210)
