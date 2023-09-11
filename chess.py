import pygame
import sys

# Función para calcular el valor basado en piezas capturadas
def value(pawn, knight, bishop, rook, queen):
    # Devuelve el valor total basado en la suma de piezas capturadas y sus respectivos valores
    return pawn + 3 * (knight + bishop) + 5 * rook + 9 * queen

def main():
    # Solicita al usuario que introduzca la cantidad de piezas capturadas de cada tipo
    pawn = int(input("how many pawns did you capture?"))
    knight = int(input("how many knights did you capture?"))
    bishop = int(input("how many bishops did you capture?"))
    rook = int(input("how many rooks did you capture?"))
    queen = int(input("how many queens did you capture?"))
    # Muestra la puntuación calculada
    print("your score is:", value(pawn, knight, bishop, rook, queen))

# Configuraciones iniciales de pygame
ANCHO, ALTO = 640, 640  # Dimensiones de la ventana
FILAS, COLUMNAS = 8, 8  # Dimensiones del tablero
TAMAÑO_CASILLA = ANCHO // COLUMNAS  # Tamaño de cada casilla del tablero

# Colores utilizados
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

def dibuja_tablero():
    # Dibuja un tablero de ajedrez en la ventana
    ventana.fill(BLANCO)  # Establece el fondo blanco
    for fila in range(FILAS):
        # Determina el color inicial de la fila
        color_actual = BLANCO if fila % 2 == 0 else NEGRO
        for col in range(COLUMNAS):
            pygame.draw.rect(ventana, color_actual, (col * TAMAÑO_CASILLA, fila * TAMAÑO_CASILLA, TAMAÑO_CASILLA, TAMAÑO_CASILLA))
            # Alterna el color para la siguiente casilla
            color_actual = NEGRO if color_actual == BLANCO else BLANCO
    pygame.display.flip()  # Actualiza la ventana

# Inicializa pygame
pygame.init()

# Crea la ventana del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tablero con Pygame")

# Dibuja el tablero inicial
dibuja_tablero()

# Bucle principal para manejar eventos
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        # Si el usuario cierra la ventana, finaliza el bucle
        if evento.type == pygame.QUIT:
            corriendo = False
            break

# Finaliza pygame
pygame.quit()

# Llama a la función main para que el usuario introduzca las piezas capturadas y muestre el resultado
main()
