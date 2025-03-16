# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
# Lista donde se guardarán los elementos
lista = []

# Pedir al usuario cuántos elementos ingresará
n = int(input("Ingrese la cantidad de elementos: "))

# Llenado de la lista
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista.append(elemento)  # Forma correcta de agregar elementos

# Implementación de QuickSort
def acomodo(lista, left, right):
    if left >= right:
        return  # Caso base de la recursión

    i, j = left, right
    x = lista[(left + right) // 2]  # Pivote

    while i <= j:
        while lista[i] < x:
            i += 1
        while lista[j] > x:
            j -= 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1

    # Llamadas recursivas
    acomodo(lista, left, j)
    acomodo(lista, i, right)

# Llamar a la función de ordenamiento
acomodo(lista, 0, len(lista) - 1)

# Imprimir lista ordenada
print("Lista ordenada:", lista)
