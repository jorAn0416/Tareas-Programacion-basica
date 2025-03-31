# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:31:59 2025

@author: Jorge Ramírez 2014275
"""
# Lista donde se guardarán los elementos
lista = []

# Pedir al usuario cuántos elementos ingresará
n = int(input("Ingrese la cantidad de elementos: "))

# Llenado de la lista
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento) 

# Se define la función con el método de inserción   
def insercion(lista):
    for i in range(1, len(lista)):  # Empezamos desde el segundo elemento
        clave = lista[i]
        j = i - 1
        
        # Mover los elementos mayores a la derecha
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = clave  
    
    return lista  # Retornar la lista ordenada

# Se llama a la función y muestra la lista ordenada
lista_ordenada = insercion(lista)
print("Lista ordenada:", lista_ordenada)
        
