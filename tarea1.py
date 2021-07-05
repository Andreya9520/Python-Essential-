#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 18:37:00 2021

@author: andreavergara
"""

#60.31143162393162 31.36194444444444 23.52145833333333 
#3.9007393587617467 7.490910297239916 10.009131205673757

#
#1 milla por galon es igual a 235.214583/100 km
#1 galon=3.785 litros
#1 milla=1,609 km 


def l100kmtompg(liters):
        mpg= (235.214583*liters)
        return mpg
                                                                                                                                                                  
def mpgtol100km(miles):
        mil= (235.214583/miles)
        return mil



print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))