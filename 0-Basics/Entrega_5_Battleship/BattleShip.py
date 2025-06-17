#Se importa la biblioteca de NumPY
import numpy as npy
#Se crea un la cuadrícula
cuadricula = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
cuadricula = npy.array(cuadricula)

chequeo = " "

#Se imprime la cuadrícula
print ("Elie cuántos barcos quieres buscar")

#Se añade los valores de la matriz
mar = " "
matriz = []

#Se imprime la matriz para los barcos
for x in range (6):
    matriz.append([])
    for y in range (6):
        matriz[x].append(mar)
matriz = npy.array(matriz)

#se imprime la matriz desde 0 hasta llegar al máximo
maximoBarcos = int(input("Por favor, indica la cantidad de barcos"))
barcos = 0

while barcos != maximoBarcos:
    barX = npy.random.randint(0,5)
    barY = npy.random.randint (0,5)
    if matriz[barX][barY] != "b":
        matriz[barX][barY] = "b"
        barcos +=1
    
