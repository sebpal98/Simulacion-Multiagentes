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

# Dimensiones de las carreteras
ROAD_WIDTH = 200
ROAD_HEIGHT = 30

# Dimensiones de las aceras
SIDEWALK_WIDTH = 60

# Espacio entre las aceras y el cebreado peatonal
SPACE_BETWEEN_SIDEWALKS = 10
CROSSWALK_WIDTH = ROAD_WIDTH - (2 * SIDEWALK_WIDTH + SPACE_BETWEEN_SIDEWALKS * 2)
CROSSWALK_HEIGHT = 20

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación de Cruce Vehicular")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

        # # Dibujar las líneas amarillas para delimitar los carriles
        # for y in range(0, HEIGHT, ROAD_HEIGHT):
        #     pygame.draw.rect(screen, YELLOW, (WIDTH/2 - ROAD_WIDTH/2, y, ROAD_WIDTH, 10))
        # for x in range(0, WIDTH, ROAD_HEIGHT):
        #     pygame.draw.rect(screen, YELLOW, (x, HEIGHT/2 - ROAD_WIDTH/2, 10, ROAD_WIDTH))

        # Dibujar las aceras

        # # Dibujar el cebreado peatonal en cada acera
        # pygame.draw.rect(screen, WHITE, (WIDTH/2 - ROAD_WIDTH/2 - SIDEWALK_WIDTH, HEIGHT/2 - CROSSWALK_HEIGHT/2, SIDEWALK_WIDTH, CROSSWALK_HEIGHT))
        # pygame.draw.rect(screen, WHITE, (WIDTH/2 + ROAD_WIDTH/2, HEIGHT/2 - CROSSWALK_HEIGHT/2, SIDEWALK_WIDTH, CROSSWALK_HEIGHT))
        # pygame.draw.rect(screen, WHITE, (WIDTH/2 - CROSSWALK_HEIGHT/2, HEIGHT/2 - ROAD_WIDTH/2 - SIDEWALK_WIDTH, CROSSWALK_HEIGHT, SIDEWALK_WIDTH))
        # pygame.draw.rect(screen, WHITE, (WIDTH/2 - CROSSWALK_HEIGHT/2, HEIGHT/2 + ROAD_WIDTH/2, CROSSWALK_HEIGHT, SIDEWALK_WIDTH))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
