#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:15:01 2021

@author: andreavergara
"""

def isPrime(n): #funcion se adapte  una cantidad x de argumentos 
   for i in range(2, int(n**0.5)+1):
      if n%i==0:
          return False
   return True
                        
   
for i in range (1,20):
    if isPrime(i+1):
            print(i+1, end=" ")
print()

    
def is_prime(x):
    if x<2: 
        return False 
    elif x==2:
        return True 
    for n in range (2,x):
        if x%n==0: 
            return False 
    return True 

for i in range (1,20):
    if isPrime(i+1):
            print(i+1, end=" ")
print()
   


