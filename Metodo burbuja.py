# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:08:14 2025

@author: Jorge Ramírez 2014275
"""
# Lista donde se guardarán los elementos
lista = []

n = int(input("Ingrese la cantidad de elementos: "))

# Llenado de la lista
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)  
    
def metbu(lista):
    n = len(lista)
    for i in range(n):  
        for j in range(n - 1 - i):  
            if lista[j] > lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambio
    return lista

metbu(lista)
print(lista)
