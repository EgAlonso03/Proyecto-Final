#Estrategia 2

import time
import matplotlib.pyplot as plt
import random
import math

def inicializar_tablero(N):
    tablero = [[0 for _ in range(N)] for _ in range(N)]
    columnas = list(range(N))
    random.shuffle(columnas)
    for fila in range(N):
        col = columnas.pop()
        tablero[fila][col] = 1
    return tablero

def es_seguro(tablero, fila, col, N):
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if tablero[i][j] == 1:
                return False
        for i, j in zip(range(fila, N, 1), range(col, -1, -1)):
            if tablero[i][j] == 1:
                return False
    return True

def resolver_n_reinas_util(tablero, col, N, filas_colocadas):
    if col >= N:
        return True
    for fila in range(N):
        if fila not in filas_colocadas and es_seguro(tablero, fila, col, N):
            tablero[fila][col] = 1
            filas_colocadas.add(fila)
            if resolver_n_reinas_util(tablero, col + 1, N, filas_colocadas) == True:
                return True
            tablero[fila][col] = 0
            filas_colocadas.remove(fila)
    return False

def resolver_n_reinas(N):
    tablero = inicializar_tablero(N)
    tablero = [[0 for _ in range(N)] for _ in range(N)]
    filas_colocadas = set()
    tiempo_inicio = time.time()
    if resolver_n_reinas_util(tablero, 0, N, filas_colocadas) == False:
        print(f"No existe solución para {N}-Reinas")
        return float('inf')  
    tiempo_fin = time.time()
    print(f"Solución para {N}-Reinas:")
    imprimir_tablero(tablero)
    print(f"Tiempo de ejecución para {N}-Reinas: {tiempo_fin - tiempo_inicio:.6f} segundos\n")
    return tiempo_fin - tiempo_inicio

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))

tamaños_problema = [14, 15, 16, 17, 18]
tiempos_ejecucion = []
for tamaño in tamaños_problema:
    tiempo_ejecucion = resolver_n_reinas(tamaño)
    tiempos_ejecucion.append(tiempo_ejecucion)

plt.plot(tamaños_problema, tiempos_ejecucion, marker='o')
plt.title('Problema N-Reinas')
plt.xlabel('Tamaño del problema')
plt.ylabel('Tiempo de ejecución (s)')
plt.show()
