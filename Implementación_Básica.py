#Implementación Básica

import time
import matplotlib.pyplot as plt

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

def resolver_n_reinas_util(tablero, col, N):
    if col >= N:
        return True
    for i in range(N):
        if es_seguro(tablero, i, col, N):
            tablero[i][col] = 1
            if resolver_n_reinas_util(tablero, col + 1, N) == True:
                return True
            tablero[i][col] = 0
    return False

def resolver_n_reinas(N):
    tablero = [[0 for _ in range(N)] for _ in range(N)]
    start_time = time.time()
    if resolver_n_reinas_util(tablero, 0, N) == False:
        print(f"No existe solución para el problema de las {N} reinas")
        return float('inf')  
    end_time = time.time()
    print(f"Solución para el problema de las {N} reinas:")
    imprimir_tablero(tablero)
    print(f"Tiempo de ejecución para el problema de las {N} reinas: {end_time - start_time:.6f} segundos\n")
    return end_time - start_time

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(casilla) for casilla in fila))

tamaños_problema = [14, 15, 16, 17, 18]
tiempos_ejecucion = []
for tamaño in tamaños_problema:
    tiempo_ejecucion = resolver_n_reinas(tamaño)
    tiempos_ejecucion.append(tiempo_ejecucion)

plt.plot(tamaños_problema, tiempos_ejecucion, marker='o')
plt.title('Problema de las N reinas')
plt.xlabel('Tamaño del problema')
plt.ylabel('Tiempo de ejecución (s)')
plt.show()
