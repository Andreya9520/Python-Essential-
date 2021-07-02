#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:40:41 2021

@author: andreavergara
"""

#F0=0,F1=1,Fk=Fk−1+Fk−2,cuando k≥2.
def fibonacci (n):
    a,b=0,1
    while a < n: 
            print (a,end=" ")
            
            a,b=b, a+b
       
    print()
