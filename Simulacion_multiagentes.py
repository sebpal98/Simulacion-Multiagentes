import pygame

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (135, 206, 235)

# Dimensiones de las carreteras
ROAD_WIDTH = 200
ROAD_HEIGHT = 30

# Dimensiones de las aceras
SIDEWALK_WIDTH = 60

# Espacio entre las aceras y el cebreado peatonal
SPACE_BETWEEN_SIDEWALKS = 10
CROSSWALK_WIDTH = ROAD_WIDTH - (2 * SIDEWALK_WIDTH + SPACE_BETWEEN_SIDEWALKS * 2)
CROSSWALK_HEIGHT = 20

# Velocidad del carro
CAR_SPEED = 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación de Cruce Vehicular")

    clock = pygame.time.Clock()

    car_rect = pygame.Rect(0, 0, 30, 50)  # Rectángulo naranja para representar el carro
    car_rect.centerx = WIDTH // 2 + 50  # Posición inicial del carro en el centro de la pantalla
    car_rect.bottom = HEIGHT  # El carro comienza desde la parte inferior de la pantalla

    car_rect2 = pygame.Rect(0, 0, 30, 50)  # Rectángulo naranja para representar el segundo carro
    car_rect2.centerx = WIDTH // 2 - 50  # Posición inicial del carro en el centro de la pantalla
    car_rect2.bottom = HEIGHT - HEIGHT  # El carro comienza desde la parte inferior de la pantalla



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimiento del carro hacia arriba
        car_rect.y -= CAR_SPEED
        car_rect2.y += CAR_SPEED

        screen.fill(GREEN)

        pygame.draw.rect(screen, WHITE, (WIDTH/2 - ROAD_WIDTH/2 - SIDEWALK_WIDTH, 0, SIDEWALK_WIDTH, HEIGHT))
        pygame.draw.rect(screen, WHITE, (WIDTH/2 + ROAD_WIDTH/2, 0, SIDEWALK_WIDTH, HEIGHT))
        pygame.draw.rect(screen, WHITE, (0, HEIGHT/2 - ROAD_WIDTH/2 - SIDEWALK_WIDTH, WIDTH, SIDEWALK_WIDTH))
        pygame.draw.rect(screen, WHITE, (0, HEIGHT/2 + ROAD_WIDTH/2, WIDTH, SIDEWALK_WIDTH))

        # Dibujar las carreteras
        pygame.draw.rect(screen, GREY, (WIDTH/2 - ROAD_WIDTH/2, 0, ROAD_WIDTH, HEIGHT))
        pygame.draw.rect(screen, GREY, (0, HEIGHT/2 - ROAD_WIDTH/2, WIDTH, ROAD_WIDTH))

        # Dibujar las líneas amarillas en las carreteras
        for y in range(0, HEIGHT, 80):
            pygame.draw.rect(screen, YELLOW, (WIDTH/2 - 5, y, 10, 40))
        for x in range(0, WIDTH, 80):
            pygame.draw.rect(screen, YELLOW, (x, HEIGHT/2 - 5, 40, 10))

        # Dibujar el carro en su posición actual
        pygame.draw.rect(screen, ORANGE, car_rect)
        pygame.draw.rect(screen, BLUE, car_rect2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
