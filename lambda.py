#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:41:56 2021

@author: andreavergara
funciones anonimas
"""
def a(x,y):
    return x+y
b=lambda x,y:x+y

revertir = lambda cadena: cadena[::-1]

print(revertir("Hola"))

sumar = lambda x,y: x+y

print(sumar(5,2))

impar = lambda num: num%2 != 0

print(impar(4))

doblar = lambda num: num*2

print(doblar(2))

seq = ['data','salt' ,'dairy','cat', 'dog']

print(list(filter(lambda word: word[0]=='d',seq)))
