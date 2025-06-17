from datetime import datetime
import random

marcador1 = 0
marcador2 = 0

def  selecciona_matriz(self):
    m1 = [['    ','1','3','4','5','6','7','8'],['A','X','X','X','X','X','X','X','X'],['B','X','X','X','X','X','X','X','X'],['C','X','X','X','X','X','X','X','X']]
    m2 = [['    ','1','3','4','5','6','7','8'],['A','X','X','X','X','X','X','X','X'],['B','X','X','X','2','X','X','X','5'],['C','X','X','X','X','X','X','2','X']]
    m3 = [['    ','1','3','4','5','6','7','8'],['A','X','X','X','X','X','X','4','X'],['B','X','X','X','X','X','X','X','X'],['C','X','X','X','X','2','X','X','X']]
    m4 = [['    ','1','3','4','5','6','7','8'],['A','X','X','X','X','X','X','X','X'],['B','X','X','X','X','X','X','X','5'],['C','X','X','X','X','X','X','X','X']]
    m5 = [['    ','1','3','4','5','6','7','8'],['A','X','X','X','X','X','X','X','X'],['B','X','X','3','X','X','X','X','5'],['C','X','2','X','X','X','X','X','X']]
    m6 = [['    ','1','3','4','5','6','7','8'],['A','X','X','X','4','X','X','X','X'],['B','X','X','X','X','X','X','X','X'],['C','X','X','X','X','X','X','X','X']]
    m7 = [['    ','1','3','4','5','6','7','8'],['A','X','2','X','X','4','X','X','X'],['B','X','X','X','X','X','X','X','X'],['C','X','X','X','3','X','X','X','X']]
    m8 = [['    ','1','3','4','5','6','7','8'],['A','X','X','X','X','X','X','X','5'],['B','X','X','X','X','X','X','X','X'],['C','X','X','X','X','X','X','X','X']]
    mat = random.randint (1,8)
    print(mat)
    
    if mat ==1:
        return m1
    elif mat ==2:
        return m2
    elif mat ==3:
        return m3
    elif mat ==4:
        return m4
    elif mat ==5:
        return m5
    elif mat ==6:
        return m6
    elif mat ==7:
        return m7
    elif mat ==8:
        return m8
    
def matriz1(self):
        matriz = []
        for x in range(9):
            matriz.append([])
            for y in range(9):
                matriz[x].append('□')
        return matriz
    
def matriz2(self):
        matriz = []
        for i in range(9):
            matriz.append([])
            for j in range(9):
                matriz[i].append('□')
        return matriz
    
def  matriz_coordenadas(matriz):
        letras = 65
        numeros = 1
        for m in range(len(matriz)):
            for n in range (len(matriz[m])):
                if m == 0 and n ==0:
                    matriz[m][n] = '    '
                elif m > 0 and n == 0:
                    matriz [m][n] = chr(letras)
                    letras = letras + 1
                elif m == 0 and n > 0:
                    matriz [m][n] = "%m " % (numeros)
                    letras = letras + 1
        return matriz
    
def disparo(self, matriz001, m3, ren, col):
    for i in range(len(m3)):
        for j in range (len(m3[i])):
            if m3[i][j] == m3 [ren][col]:
                matriz001[ren][col] = m3[i][j]
    return matriz001

def revision_fila(self):
    vali = True
    while vali == True:
        ren = str(input("Selecciona una fila "))
        ren = ren.upper()
        if ren == 'A':
            ren = 1
            vali = False
        elif ren == 'B':
            ren = 2
            vali = False
        elif ren == 'C':
            ren = 3
            vali = False
        else:
            print("La opcion no es válida, intenta nuevamente ")
    return ren 

def revision_columna():
    vali = True
    while vali == True:
        columna = int(input("Selecciona una Columna "))
        if columna > 0 and columna < 9:
            vali = False
        else:
            print("La opcion no es válida, intenta nuevamente ")
    return columna

def impresion_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(matriz[i]):
            print("%3s" %  matriz[i][j], end=' ')
        print()
        
def aciertos_barco(matriz002, m3, ren ,col):
    for i in range(len(m3)):
        for j in range(len(m3[i])):
            if m3 [i][j] == m3[ren][col] and m3[i][j] == 2:
                tiro = True
                return tiro
            elif m3[i][j] == m3 [ren][col] and m3 [i][j] == 3:
                tiro = True
                return tiro 
            elif m3[i][j] == m3 [ren][col] and m3 [i][j] == 4:
                tiro = True
                return tiro
            elif m3[i][j] == m3 [ren][col] and m3 [i][j] == 5:
                tiro = True
                return tiro
            elif m3[i][j] == m3 [ren][col] and m3 [i][j] == X:
                tiro = False
                return tiro  
            
def derrivos_nave (matriz, ren, col, a2, a3, a4, a5):
    if matriz[ren][col] == 2:
        a2 = a2 + 1  
    elif matriz[ren][col] == 3:
        a3 = a3 + 1
    elif matriz[ren][col] == 4:
        a4 = a4 + 1
    elif matriz[ren][col] == 5:
        a5 = a5 + 1
    else:
        return a2, a3, a4, a5
    
def impresion_victoria(jugador):
    print("Felicidades %s!"%jugador)
    print()
    
def tiro_repetido(matriz, ren , col):
    bien == True
    while bien == True:
        if matriz [i][j] == matriz[ren][col]:
            print("No hay nada ahi...")
            bien = True
        elif matriz [i][j] == matriz[ren][col]:
            bien = False
            
def menu():
    print("1. un jugador")
    
def juego_principal():
    juego = '0'
    sigue = True
    while sigue == True:
        menu()
        juego = str(input("1 para jugar"))
        juego = juego.upper()
        if juego == '1':
            unJugador = str(input("Ingresa tu nombre: "))
            a2 = 0
            a3 = 0
            a4 = 0
            a5 = 0
            marcador1 = 0
            ronda1 = 1
            mat = matriz1()
            mi_matriz = selecciona_matriz(mat)
            mat = selecciona_matriz()
            print()
            impresion_matriz(mi_matriz)
            for i in range(10):
                print()
                print("Ronda %i" %ronda1)
                print()
                ronda1 = ronda1 + 1
                for i in range(3):
                    bien = True
                    while bien == True:
                        ren = revision_fila()
                        col = revision_columna()
                        matriz2 = mat
                        if mi_matriz[ren][col] == '□':
                            bien = False
                        elif  mi_matriz[ren][col] == '□':
                            bien = False
                        else:
                            bien = True
                            print("Ya habías tirado ahí...")
        
    
    
        