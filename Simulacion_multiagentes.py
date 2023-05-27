import pygame

# Dimensiones de la ventana
WIDTH = 1200
HEIGHT = 800

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (135, 206, 235)
RED = (255, 0, 0)
GREEN_LIGHT = (0, 255, 0)

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


class Carro:
    def __init__(self, x, y, width, height, color, direction):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.direction = direction

    def move(self):
        if self.direction == 'up':
            self.rect.y -= CAR_SPEED
        elif self.direction == 'down':
            self.rect.y += CAR_SPEED
        elif self.direction == 'left':
            self.rect.x -= CAR_SPEED
        elif self.direction == 'right':
            self.rect.x += CAR_SPEED

    def check_collision(self, rect):
        return self.rect.colliderect(rect)


class Semaforo:
    LIGHT_COLOR = (255, 0, 0)  # Rojo
    COLLIDER_COLOR = (0, 0, 255, 20)  # Azul transparente

    def __init__(self, x_light, y_light,light_size , x_collider,y_collider, collider_size):
        self.color = Semaforo.LIGHT_COLOR
        self.light_rect = pygame.Rect(x_light, y_light, light_size[0], light_size[1])
        self.collider_rect = pygame.Rect(x_collider, y_collider, collider_size[0], collider_size[1])

    def change_color(self):
        if self.color == Semaforo.LIGHT_COLOR:
            self.color = (0, 255, 0)  # Verde
        else:
            self.color = Semaforo.LIGHT_COLOR

    def is_red(self):
        return self.color == Semaforo.LIGHT_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, Semaforo.COLLIDER_COLOR, self.collider_rect)
        pygame.draw.rect(screen, self.color, self.light_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación de Cruce Vehicular")

    clock = pygame.time.Clock()
    # Crea un carro en la posicion  x, y, width, height, color, direction):
    car1 = Carro(650, 790, 30, 50, ORANGE, 'up')
    car2 = Carro(1200,340, 50, 30, YELLOW, 'left')
    car3 = Carro(540,0, 30, 50, BLUE, 'down')
    car4 = Carro(0,450, 50, 30, WHITE, 'right')


    # Crear un semáforo en la posición (x, y, y luz de tamaño (20, 40) ) con colisionador de tamaño (x, y, de tamaño (20, 40) )
    semaforo1 = Semaforo(640, 500, (20, 20), 620, 500,(60, 50))
    semaforo2 = Semaforo(550, 280, (20, 20), 530, 250,(60, 50))
    semaforo3 = Semaforo(700, 340, (20, 20), 700, 320,(50, 60))
    semaforo4 = Semaforo(480, 440, (20, 20), 450, 420,(50, 60))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimiento de los carros
        car1.move()
        car2.move()
        car3.move()
        car4.move()

        screen.fill(GREEN)

        pygame.draw.rect(screen, WHITE, (WIDTH/2 - ROAD_WIDTH/2 - SIDEWALK_WIDTH, 0, SIDEWALK_WIDTH, HEIGHT))
        pygame.draw.rect(screen, WHITE, (WIDTH/2 + ROAD_WIDTH/2, 0, SIDEWALK_WIDTH, HEIGHT))
        pygame.draw.rect(screen, WHITE, (0, HEIGHT/2 - ROAD_WIDTH/2 - SIDEWALK_WIDTH, WIDTH, SIDEWALK_WIDTH))
        pygame.draw.rect(screen, WHITE, (0, HEIGHT/2 + ROAD_WIDTH/2, WIDTH, SIDEWALK_WIDTH))

        pygame.draw.rect(screen, GREY, (WIDTH/2 - ROAD_WIDTH/2, 0, ROAD_WIDTH, HEIGHT))
        pygame.draw.rect(screen, GREY, (0, HEIGHT/2 - ROAD_WIDTH/2, WIDTH, ROAD_WIDTH))

        for y in range(0, HEIGHT, 80):
            pygame.draw.rect(screen, YELLOW, (WIDTH/2 - 5, y, 10, 40))
        for x in range(0, WIDTH, 80):
            pygame.draw.rect(screen, YELLOW, (x, HEIGHT/2 - 5, 40, 10))

        pygame.draw.rect(screen, car1.color, car1.rect)
        pygame.draw.rect(screen, car2.color, car2.rect)
        pygame.draw.rect(screen, car3.color, car3.rect)
        pygame.draw.rect(screen, car4.color, car4.rect)

        semaforo1.draw(screen)
        semaforo2.draw(screen)
        semaforo3.draw(screen)
        semaforo4.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
