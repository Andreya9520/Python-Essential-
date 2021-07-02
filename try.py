#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:22:04 2021

@author: andreavergara
"""
"""
try: 
    print("Inicio")
    x=1/0
    print("Proceso")
except: 
    print ("Hay un error")
print("fin")
"""

try: 
    x=int (input("Enter a number: "))
    y=1/x
    print(y)
except ZeroDivisionError: 
    print("You cannot divide by zero, sorry.")
except ValueError: 
    print("You must enter an integer value.") 
except:
    print("Oh dear, something went wrong....")
print("The end. ")