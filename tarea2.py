#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 20:08:43 2021

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

#

 

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
            yr = testData[i]
            print(yr,"->",end="")
            result = isYearLeap(yr)
            if result == testResults[i]:

                        print("OK")
            else:
                        print("Failed")