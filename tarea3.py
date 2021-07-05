#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:02:09 2021

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
 
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
                yr = testYears[i]
                mo = testMonths[i]
                print(yr, mo, "->", end="")
                result = daysInMonth(yr, mo)
                if result == testResults[i]:
                                print("OK")
                else:
                                print("Failed")
                            
                                