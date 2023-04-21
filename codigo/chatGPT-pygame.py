import pygame

# Inicializa Pygame
pygame.init()

# Crea una ventana de juego de tamaño 800x600
window = pygame.display.set_mode((800, 600))

# Clase que representa el rectángulo que controlarás en el juego
class Rectangle:
    def __init__(self):
        # La posición inicial del rectángulo es (100, 100)
        self.x = 100
        self.y = 100
        
        # El tamaño del rectángulo es (50, 50)
        self.width = 50
        self.height = 50

    def update(self, keys):
        # Si se presiona la tecla de flecha hacia la izquierda, mueve el rectángulo hacia la izquierda
        if keys[pygame.K_LEFT]:
            self.x -= 5

        # Si se presiona la tecla de flecha hacia la derecha, mueve el rectángulo hacia la derecha
        if keys[pygame.K_RIGHT]:
            self.x += 5

        # Si se presiona la tecla de flecha hacia arriba, mueve el rectángulo hacia arriba
        if keys[pygame.K_UP]:
            self.y -= 5

        # Si se presiona la tecla de flecha hacia abajo, mueve el rectángulo hacia abajo
        if keys[pygame.K_DOWN]:
            self.y += 5

# Crea una instancia de la clase rectángulo
rectangle = Rectangle()

#Ciclo principal del juego
while True:
    # Maneja los eventos de Pygame
    for event in pygame.event.get():
        # Si se presiona una tecla, detecta qué tecla es
        if event.type == pygame.KEYDOWN:
            # Si se presiona la tecla de escape, sale del juego
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Si se libera una tecla, detecta qué tecla es
        if event.type == pygame.KEYUP:
        # Aquí puedes agregar código para detectar cuando se libera una tecla
            pass
        
    # Obtiene el estado de todas las teclas del teclado
    keys = pygame.key.get_pressed()

    # Actualiza la posición del rectángulo en función de las teclas presionadas
    rectangle.update(keys)

    # Rellenamos el fondo de negro
    window.fill((0,0,0))

    # Dibuja el rectángulo en la pantalla
    pygame.draw.rect(window, (255, 0, 0), (rectangle.x, rectangle.y, rectangle.width, rectangle.height))

    # Actualiza la pantalla
    pygame.display.update()                
