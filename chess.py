import pygame
import sys

# Función simplificada para calcular el valor
def value(pawn, knight, bishop, rook, queen):
    return pawn + 3 * (knight + bishop) + 5 * rook + 9 * queen

def main():
    pawn = int(input("how many pawns did you capture?"))
    knight = int(input("how many knights did you capture?"))
    bishop = int(input("how many bishops did you capture?"))
    rook = int(input("how many rooks did you capture?"))
    queen = int(input("how many queens did you capture?"))
    print("your score is:", value(pawn, knight, bishop, rook, queen))

# Configuraciones de pygame
ANCHO, ALTO = 640, 640
FILAS, COLUMNAS = 8, 8
TAMAÑO_CASILLA = ANCHO // COLUMNAS

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

def dibuja_tablero():
    ventana.fill(BLANCO)
    for fila in range(FILAS):
        color_actual = BLANCO if fila % 2 == 0 else NEGRO
        for col in range(COLUMNAS):
            pygame.draw.rect(ventana, color_actual, (col * TAMAÑO_CASILLA, fila * TAMAÑO_CASILLA, TAMAÑO_CASILLA, TAMAÑO_CASILLA))
            color_actual = NEGRO if color_actual == BLANCO else BLANCO
    pygame.display.flip()

pygame.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tablero con Pygame")

dibuja_tablero()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            break

pygame.quit()

# Ahora llamamos a main para que el usuario introduzca las piezas capturadas
main()
