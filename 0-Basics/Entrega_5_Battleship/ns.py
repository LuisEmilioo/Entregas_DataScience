import random

class Tablero:
    def __init__(self, tamaño=5): #se crea el tablero
        self.tamaño = tamaño
        self.tablero = [["□"] * tamaño for _ in range(tamaño)]

    def mostrar(self, ocultar_barcos=False): #se imprimer el tablero con iconos de un cuadrado
        print("  " + " ".join(str(i) for i in range(self.tamaño)))
        for i, fila in enumerate(self.tablero):
            fila_visible = []
            for celda in fila:
                if ocultar_barcos and celda == "B":
                    fila_visible.append("□")
                else:
                    fila_visible.append(celda)
            print(f"{i} " + " ".join(fila_visible))# f según internet es para formatear y permite insertar variable

    def colocar_barco(self, fila, columna):#muestra tu barco
        self.tablero[fila][columna] = "B"

    def recibir_disparo(self, fila, columna):
        if self.tablero[fila][columna] == "B":
            self.tablero[fila][columna] = "X"
            print("Hundido")
            return True
        elif self.tablero[fila][columna] == "□":
            self.tablero[fila][columna] = "≋"
            print("Agua ")
            return False
        else:
            print("Ya has disparado aquí.")
            return False

    def barco_hundido(self):
        for fila in self.tablero:
            if "B" in fila:
                return False
        return True


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()
        self.barco_fila = random.randint(0, 4)
        self.barco_columna = random.randint(0, 4)
        self.tablero.colocar_barco(self.barco_fila, self.barco_columna)

    def disparar(self, enemigo):
        try:
            fila = int(input(f"{self.nombre}, elige fila: "))
            columna = int(input(f"{self.nombre}, elige columna: "))
            if 0 <= fila <= 4 and 0 <= columna <= 4:
                return enemigo.tablero.recibir_disparo(fila, columna)
            else:
                print("Coordenadas fuera de rango ")
        except ValueError:
            print("Entrada inválida")
        return False


class Juego:
    def __init__(self):
        self.jugador = Jugador("Jugador")
        self.computadora = Jugador("Computadora")

    def jugar(self):
        print("¡Bienvenido a Batalla Naval!")
        turno = 0
        while True:
            print("\nTu tablero:")
            self.jugador.tablero.mostrar()
            print("\nTablero enemigo:")
            self.computadora.tablero.mostrar(ocultar_barcos=True)

            if turno % 2 == 0:
                print("\n Tu turno")
                self.jugador.disparar(self.computadora)
            else:
                print("\n Turno de la computadora")
                fila = random.randint(0, 4)
                columna = random.randint(0, 4)
                print(f"La computadora dispara a ({fila}, {columna})")
                self.jugador.tablero.recibir_disparo(fila, columna)

            if self.computadora.tablero.barco_hundido():
                print("¡Ganaste! ")
                break
            elif self.jugador.tablero.barco_hundido():
                print("Perdiste ")
                break

            turno += 1

# Ejecutar____________________________________________________________________
if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
