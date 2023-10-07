import pygame
import sys

# Función para calcular el valor basado en piezas capturadas
def value(pieces):
    values = {'pawn': 1, 'knight': 3, 'bishop': 3, 'rook': 5, 'queen': 9}
    return sum(values[piece] * count for piece, count in pieces.items())

def main():
    # Usamos un diccionario para almacenar las piezas y evitar repetir código
    pieces = {
        'pawn': 0,
        'knight': 0,
        'bishop': 0,
        'rook': 0,
        'queen': 0
    }

    for piece in pieces.keys():
        pieces[piece] = int(input(f"how many {piece}s did you capture?"))

    # Muestra la puntuación calculada
    print(f"your score is: {value(pieces)}")

# Configuraciones iniciales de pygame
ANCHO, ALTO = 640, 640
FILAS, COLUMNAS = 8, 8
TAMAÑO_CASILLA = ANCHO // COLUMNAS

# Colores utilizados
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Matriz para representar el tablero
# Por ahora está vacío, pero puedes poner piezas en él
# Ejemplo: tablero[0][0] = 'pawn' representa un peón en la esquina superior izquierda
tablero = [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]

def dibuja_tablero():
    ventana.fill(BLANCO)
    for fila in range(FILAS):
        color_actual = BLANCO if fila % 2 == 0 else NEGRO
        for col in range(COLUMNAS):
            pygame.draw.rect(ventana, color_actual, (col * TAMAÑO_CASILLA, fila * TAMAÑO_CASILLA, TAMAÑO_CASILLA, TAMAÑO_CASILLA))
            color_actual = NEGRO if color_actual == BLANCO else BLANCO
            # Si hay una pieza en la casilla, la dibujas (aquí solo es un ejemplo de cómo hacerlo)
            if tablero[fila][col]:
                piece_text = font.render(tablero[fila][col], True, (255,0,0))  # Renderiza el nombre de la pieza como texto
                ventana.blit(piece_text, (col * TAMAÑO_CASILLA + TAMAÑO_CASILLA // 4, fila * TAMAÑO_CASILLA + TAMAÑO_CASILLA // 4))

    pygame.display.flip()

pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tablero con Pygame")
font = pygame.font.SysFont(None, 36)  # Fuente para dibujar texto (piezas en este caso)

dibuja_tablero()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            break

pygame.quit()
main()

