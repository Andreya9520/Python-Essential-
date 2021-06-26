#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:27:48 2021

@author: andreavergara
"""

print("Estimado usuario, a continuación vamos a solicitar informacion para ingresar a la base de datos.") 
print("Gracias por su atención")
    
nombre=input("Ingrese su primer nombre:  ")
apellido=input("Ingrese su primer apellido:  ")
ubicacion=input("Ingrese la ubicacion de su vivienda(Ciudad,Pais):  ")
edad=input("Ingrese su edad: ")

print ("La informacion registrada es la siguiente:  ")
print("Su nombre es; ", nombre)
print("Su apellido es: ",apellido)
print("Su ubicación es:  ", ubicacion)
print ("Su edad es:   ",edad,"años")

confirmacion=input("¿La información registrada es correcta?: ")
print("Gracias por su colaboración")