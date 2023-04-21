# prompt: crea un programa videojuego en python usando pygame para controlar un rectángulo de 37 x 37 pixels de color azul claro en una pantalla de 800 x 500 pixels  con el teclado evitando que el rectángulo salga de la pantalla

import pygame

# Inicializamos pygame
pygame.init()

# Creamos la ventana
ventana = pygame.display.set_mode((800, 500))

# Creamos el rectángulo
rectangulo = pygame.Rect(0, 0, 37, 37)
rectangulo.center = (400, 250) # Centramos el rectángulo en la pantalla

# Creamos el color azul claro
azul_claro = (0, 150, 255)

# Bandera para controlar el ciclo del juego
juego_en_curso = True

while juego_en_curso:
    # Obtenemos la lista de eventos
    eventos = pygame.event.get()
    # Recorremos la lista de eventos
    for evento in eventos:
        # Si se presiona la tecla de salida, terminamos el juego
        if evento.type == pygame.QUIT:
            juego_en_curso = False

    # Obtenemos el estado de las teclas presionadas
    teclas_presionadas = pygame.key.get_pressed()
    # Si se presiona la tecla de arriba, movemos el rectángulo hacia arriba
    if teclas_presionadas[pygame.K_UP]:
        rectangulo.y -= 5
    # Si se presiona la tecla de abajo, movemos el rectángulo hacia abajo
    if teclas_presionadas[pygame.K_DOWN]:
        rectangulo.y += 5
    # Si se presiona la tecla de izquierda, movemos el rectángulo hacia la izquierda
    if teclas_presionadas[pygame.K_LEFT]:
        rectangulo.x -= 5
    # Si se presiona la tecla de derecha, movemos el rectángulo hacia la derecha
    if teclas_presionadas[pygame.K_RIGHT]:
        rectangulo.x += 5

    # Validamos que el rectángulo no salga de la pantalla
    if rectangulo.left < 0:
        rectangulo.left = 0
    if rectangulo.right > 800:
        rectangulo.right = 800
    if rectangulo.top < 0:
        rectangulo.top = 0
    if rectangulo.bottom > 500:
        rectangulo.bottom = 500

    # Limpiamos la pantalla
    ventana.fill((0, 0, 0))
    # Dibujamos el rectángulo en la pantalla
    pygame.draw.rect(ventana, azul_claro, rectangulo)
    # Actualizamos la pantalla
    pygame.display.update()

# Finalizamos pygame
pygame.quit()