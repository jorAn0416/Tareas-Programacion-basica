# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 22:45:24 2025

@author: USER
"""

def solve():
    with open('backforth.in', 'r') as f:
        barn1 = list(map(int, f.readline().split()))
        barn2 = list(map(int, f.readline().split()))
    
    results = set()
    
    def dfs(day, amount1, amount2, b1, b2):
        if day == 4:
            results.add(amount1)
            return
        
        if day % 2 == 0:  # Para día par: mover de barn1 a barn2
            for i in range(len(b1)):
                new_b1 = b1[:i] + b1[i+1:]
                new_b2 = b2 + [b1[i]]
                dfs(day + 1, amount1 - b1[i], amount2 + b1[i], new_b1, new_b2)
        else:  # Día impar: mover de barn2 a barn1
            for i in range(len(b2)):
                new_b2 = b2[:i] + b2[i+1:]
                new_b1 = b1 + [b2[i]]
                dfs(day + 1, amount1 + b2[i], amount2 - b2[i], new_b1, new_b2)
    
    dfs(0, 1000, 1000, barn1, barn2)

    with open('backforth.out', 'w') as f:
        f.write(f"{len(results)}\n")

# Ejecutar función
solve()
