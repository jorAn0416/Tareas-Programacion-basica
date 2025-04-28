# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 17:58:15 2025

@author: USER
"""
N = int(input())
vacas = []
for i in range(N):
    x, y, d = input().split()
    x, y = int(x), int(y)
    vacas.append({'id': i, 'x': x, 'y': y, 'dir': d, 'comidas': 0, 'stop': False, 'inf': False})

# Pasto que ya ha sido comido
pasto_comido = set()
# Vacas que se mueven infinitamente
infinitas = set()

# Límite máximo de pasos a simular
MAX_STEPS = 3000  # suficientemente grande para detectar infinitos

# Registro de posiciones de cada vaca con tiempo
tiempos = [{} for _ in range(N)]

for step in range(MAX_STEPS):
    movimientos = {}
    for v in vacas:
        if v['stop'] or v['inf']:
            continue
        pos = (v['x'], v['y'])

        # Verificar si el pasto ya fue comido
        if pos in pasto_comido:
            v['stop'] = True
            continue

        # Registrar que come el pasto
        pasto_comido.add(pos)
        v['comidas'] += 1

        # Guardar visita
        tiempos[v['id']][pos] = step

        # Preparar siguiente movimiento
        if v['dir'] == 'N':
            v['y'] += 1
        elif v['dir'] == 'E':
            v['x'] += 1

    # Verificamos si alguna vaca ya lleva mucho sin detenerse
    for v in vacas:
        if not v['stop'] and step == MAX_STEPS - 1:
            v['inf'] = True

# Mostrar resultados
for v in vacas:
    if v['inf']:
        print("Infinity")
    else:
        print(v['comidas'])


