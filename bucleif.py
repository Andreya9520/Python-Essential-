#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:22:42 2021

@author: andreavergara
"""

"""
Bucle IF 
Else es un condicional que va en ligar de else 

"""
nativa=1
datos=100

if datos==nativa: 
    print("The native and data are the same")
    if datos==nativa: 
        print("The native and data are the same")
        if datos==nativa: 
            print("The native and data are the same")
    
else: 
    print("The Vlans are different")
    
    """
    Elif nos permite trabajar sin la identacion multiple 
    que nos permite evaluar como que fuera un if normar una condicion
    debe ser evaluada para la parte de falso
    """
    
acl=int(input("Ingrese el # de ACL "))
if acl >=1 and acl <=99:
    print ("la ACL es Estandar")
elif acl >=100 and acl <=199:
    print ("La ACL es Extendida")
else: 
    print("El # ingresado no es de ACL")