# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 14:26:00 2025

@author: USER
"""
#Escrito por tu papá Jorge Ramírez
#20124275

# Pedir al usuario el numero a operar
n = int(input("ingresa tu nuemero del que quiera factorial"))
#definir fact igual a 1
fact=n
#iniciar el ciclo para factorial
while n > 1:
    fact*=n-1
    n-=1
print ("=",fact)
