#Optimización especifica: Estrategia 1

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

def resolver_n_reinas_util(tablero, col, N, filas_colocadas):
    if col >= N:
        return True
    for i in range(N):
        if i not in filas_colocadas and es_seguro(tablero, i, col, N):
            tablero[i][col] = 1
            filas_colocadas.add(i)
            if resolver_n_reinas_util(tablero, col + 1, N, filas_colocadas) == True:
                return True
            tablero[i][col] = 0
            filas_colocadas.remove(i)
    return False

def resolver_n_reinas(N):
    tablero = [[0 for _ in range(N)] for _ in range(N)]
    filas_colocadas = set()
    tiempo_inicio = time.time()
    if resolver_n_reinas_util(tablero, 0, N, filas_colocadas) == False:
        print(f"No existe solución para el problema de las {N} reinas")
        return float('inf')  
    tiempo_fin = time.time()
    print(f"Solución para el problema de las {N} reinas:")
    imprimir_tablero(tablero)
    print(f"Tiempo de ejecución para el problema de las {N} reinas: {tiempo_fin - tiempo_inicio:.6f} segundos\n")
    return tiempo_fin - tiempo_inicio

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
