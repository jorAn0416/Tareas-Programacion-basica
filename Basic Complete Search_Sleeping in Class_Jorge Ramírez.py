# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 22:22:28 2025

@author: USER
"""

# Lista donde se guardarán los elementos
a = []

# Pedir al usuario el numero de periodos
n = int(input("Ingrese la cantidad de periodos: "))

# Llenado de la lista
for i in range(n):
    elemento = int(input(f"Cuantas veces se durmió en el periodo {i + 1}? : "))
    a.append(elemento) 

#Se crea una función que calculara las menores modificaciones
def min_mods(a):
    n = len(a)
    total_sum = sum(a)

    # Probar posibles números de partes
    for k in range(n, 0, -1):
        if total_sum % k != 0:
            continue
        
        obj= total_sum // k
        current_sum = 0
        posible = True

        for num in a:
            current_sum += num
            if current_sum > obj:
                posible = False
                break
            if current_sum == obj:
                current_sum = 0
        
        if posible:
            return n - k

print(min_mods(a), "es el minimo de modificaciones")