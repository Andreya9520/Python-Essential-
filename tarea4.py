#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:55:21 2021

@author: andreavergara
"""

def isYearLeap(year):
    if year % 400==0:
        return True
    elif year % 100==1:
        return False 
    elif year %4==0:
        return True
    else: 
        return False 
 

def daysInMonth(year, month):
    
    diasMeses = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(year):
        if diasMeses[month - 1] == 28:
            return 29
        else:
            return diasMeses[month - 1]
    else:
        return diasMeses[month - 1]
    return None
 

def dayOfYear(year, month, day):
    
    diasSemana=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    if day>0 and day<366:
        if (day<=7):   
            return diasSemana[day-1]
        elif(day%7)==0:
            return diasSemana[6]
        else:
            return diasSemana[(day-1)%7]
        

print(dayOfYear(2000, 12, 31))
print(dayOfYear(1995,5,20))
print(dayOfYear(1970,7,5))
