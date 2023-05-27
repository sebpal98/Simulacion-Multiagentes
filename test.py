import pygame

# Configuración de la ventana
window_width = 1200
window_height = 800

# Configuración de la cuadrícula
grid_size = 10
grid_color = (200, 200, 200)  # Color de la cuadrícula en formato RGB

# Configuración de los elementos adicionales
road_width = 200
sidewalk_width = 100
green_color = (0, 255, 0)
white_color = (255, 255, 255)
grey_color = (128, 128, 128)
yellow_color = (255, 255, 0)

# Inicializar pygame y la ventana
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cuadrícula con elementos adicionales")

def draw_grid():
    # Dibujar líneas verticales
    for x in range(0, window_width, grid_size):
        pygame.draw.line(window, grid_color, (x, 0), (x, window_height))

    # Dibujar líneas horizontales
    for y in range(0, window_height, grid_size):
        pygame.draw.line(window, grid_color, (0, y), (window_width, y))

def draw_elements():
    # Dibujar los elementos adicionales
    pygame.draw.rect(window, white_color, (window_width/2 - road_width/2 - sidewalk_width, 0, sidewalk_width, window_height))
    pygame.draw.rect(window, white_color, (window_width/2 + road_width/2, 0, sidewalk_width, window_height))
    pygame.draw.rect(window, white_color, (0, window_height/2 - road_width/2 - sidewalk_width, window_width, sidewalk_width))
    pygame.draw.rect(window, white_color, (0, window_height/2 + road_width/2, window_width, sidewalk_width))

    pygame.draw.rect(window, grey_color, (window_width/2 - road_width/2, 0, road_width, window_height))
    pygame.draw.rect(window, grey_color, (0, window_height/2 - road_width/2, window_width, road_width))

    for y in range(0, window_height, 80):
        pygame.draw.rect(window, yellow_color, (window_width/2 - 5, y, 10, 40))
    for x in range(0, window_width, 80):
        pygame.draw.rect(window, yellow_color, (x, window_height/2 - 5, 40, 10))

# Bucle principal del programa
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las coordenadas del cursor relativas a la cuadrícula
    mouse_x, mouse_y = pygame.mouse.get_pos()
    grid_x = (mouse_x // grid_size) * grid_size
    grid_y = (mouse_y // grid_size) * grid_size

    # Rellenar la ventana con color verde
    window.fill(green_color)

    # Dibujar los elementos adicionales
    draw_elements()

    # Dibujar la cuadrícula
    draw_grid()

    # Mostrar las coordenadas del cursor en la cuadrícula
    font = pygame.font.Font(None, 30)
    text = font.render(f"({grid_x}, {grid_y})", True, white_color)
    window.blit(text, (10, 10))

    # Actualizar la ventana
    pygame.display.flip()

# Cerrar pygame al salir
pygame.quit()
