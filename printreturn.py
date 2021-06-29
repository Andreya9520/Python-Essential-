#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:46:07 2021

@author: andreavergara
"""
"""
def resta(a,b):
    print ("\t","El resultado de restar: ",a,"-",b,"es: ",a-b,"\n")
resta(5,2)
resta(2,5)
resta(a=2,b=5)
resta(b=3,a=15.3)
resta(3,b=15)
"""
def mult(a,b):
    #print(a*b)
    return(a*b, a+b, a/b, a**b,a//b,a%b) #cuando no hay argumento saca none, reemplaza al print 

resultado=mult(5,5)
print(resultado)
#print (mult(5,5))

def hieverybody (lista):
    for i in lista:
        print("Hola, ",i)
        
hieverybody (["Juan"])
hieverybody (["Juan","Ana"])
hieverybody (["Juan","Andrea","Jorge"])
hieverybody (["Juan","Alex","Julio","Sandra"])

def crealista(n): 
    lista1=[]
    for i in range (n): 
        lista1.append (i)
    return lista1
l=crealista(5)
print(crealista(10))

