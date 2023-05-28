import pygame

# Dimensiones de la ventana
window_width = 1200
window_height = 800

# Colores
BLACK = (0, 0, 0)
GREEN = (36, 202, 61)
GREY_ROAD = (54, 59, 55)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (135, 206, 235)
RED = (255, 0, 0)
GREEN_LIGHT = (0, 255, 0)

# Dimensiones de las carreteras
ROAD_WIDTH = 120
ROAD_HEIGHT = 30

# Dimensiones de las aceras
sidewalk_width = 20

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simulación de Cruce Vehicular")
clock = pygame.time.Clock()


class Semaforo:
    LIGHT_COLOR = (255, 0, 0)  # Rojo
    COLLIDER_COLOR = (0, 0, 255, 20)  # Azul transparente

    def _init_(self, x_light, y_light,light_size , x_collider,y_collider, collider_size):
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


def draw_elements():
    roads()
    cross_walks()
    
def roads():
    # Primera carretera  VERTICAL de izquierda a derecha
    pygame.draw.rect(window, WHITE, (130, 0, sidewalk_width, window_height))
    pygame.draw.rect(window, GREY_ROAD, (150, 0, ROAD_WIDTH, window_height))
    pygame.draw.rect(window, WHITE, (270, 0, sidewalk_width, window_height))
    
    
    for y in range(0, window_height, 20):
        pygame.draw.rect(window, YELLOW, (205, y, 5, 10))
        
    # Segunda carretera  VERTICAL de izquierda a derecha
    pygame.draw.rect(window, WHITE, (530, 0, sidewalk_width, window_height))
    pygame.draw.rect(window, GREY_ROAD, (550 , 0, ROAD_WIDTH, window_height))
    pygame.draw.rect(window, WHITE, (670, 0, sidewalk_width, window_height))
    for y in range(0, window_height, 20):
        pygame.draw.rect(window, YELLOW, (605, y, 5, 10))
    
    # Tercera carretera  VERTICAL de izquierda a derecha
    pygame.draw.rect(window, WHITE, (930, 0, sidewalk_width, window_height))
    pygame.draw.rect(window, GREY_ROAD, (950 , 0, ROAD_WIDTH, window_height))
    pygame.draw.rect(window, WHITE, (1070, 0, sidewalk_width, window_height))
    for y in range(0, window_height, 20):
        pygame.draw.rect(window, YELLOW, (1005, y, 5, 10))
    
    # Primera carretera  HORIZONTAL
    pygame.draw.rect(window, WHITE, (0, 130, window_width, sidewalk_width))
    pygame.draw.rect(window, GREY_ROAD, (0, 150, window_width, ROAD_WIDTH))
    pygame.draw.rect(window, WHITE, (0, 270, window_width, sidewalk_width))
    for y in range(0, window_width, 20):
        pygame.draw.rect(window, YELLOW, ( y,205, 10, 5))
    
    # Primera carretera  HORIZONTAL
    pygame.draw.rect(window, WHITE, (0, 530, window_width, sidewalk_width))
    pygame.draw.rect(window, GREY_ROAD, (0, 550, window_width, ROAD_WIDTH))
    pygame.draw.rect(window, WHITE, (0, 670, window_width, sidewalk_width))
    for y in range(0, window_width, 20):
        pygame.draw.rect(window, YELLOW, (y, 605, 10, 5))
        
    arrows()
        
def arrows():
    constant_roads = 400
    for y in range(80, window_width, 360):
        #Dibujar las flechas Horizontales
        pygame.draw.rect(window, WHITE, (y-30, 238, 30, 5))    
        pygame.draw.polygon(window, WHITE, ([y,240],[y-5,230],[y+15,240],[y-5,250]))
        # Fibujar las felchas izquierda
        pygame.draw.rect(window, WHITE, (y, 168, 30, 5))    
        pygame.draw.polygon(window, WHITE, ([y,170],[y+5,160],[y-15,170],[y+5,180]))

        pygame.draw.rect(window, WHITE, (y-30, 238+constant_roads, 30, 5))    
        pygame.draw.polygon(window, WHITE, ([y,240+constant_roads],[y-5,230+constant_roads],[y+15,240+constant_roads],[y-5,250+constant_roads]))
        # Fibujar las felchas izquierda
        pygame.draw.rect(window, WHITE, (y, 168+constant_roads, 30, 5))    
        pygame.draw.polygon(window, WHITE, ([y,170+constant_roads],[y+5,160+constant_roads],[y-15,170+constant_roads],[y+5,180+constant_roads]))
        
        # Dibujar flechas verticales
    for y in range(40, window_height, 260):
        #Dibujar las flechas Horizontales
        pygame.draw.rect(window, WHITE, (170, y-2, 5, 30))    
        pygame.draw.polygon(window, RED, ([170,y+30],[180,y+25],[170,y+50],[160,y+25]))


def cross_walks():
     # Inersecciones y sus cebras
    def crosswalk_x(origin_x, origin_y ):
        for y in range(origin_x, origin_x+ROAD_WIDTH, 10):
            pygame.draw.rect(window, GREY_ROAD, (y, origin_y, 6, 20))

    def crosswalk_y(origin_x, origin_y):
        for y in range(origin_y, origin_y + ROAD_WIDTH, 10):
            pygame.draw.rect(window, WHITE, (origin_x, y, 20, 6))
    
    #Primer interseccion
    pygame.draw.rect(window, GREY_ROAD, (130, 150, ROAD_WIDTH+40, ROAD_WIDTH))
    # Horizontales
    crosswalk_x(150, 130) 
    crosswalk_x(150, 270)
    # Verticales
    crosswalk_y(130, 150)
    crosswalk_y(270, 150)
    
    # Segunda interseccion
    pygame.draw.rect(window, GREY_ROAD, (530, 150, ROAD_WIDTH+40, ROAD_WIDTH))
    # Horizontales
    crosswalk_x(150, 530)
    crosswalk_x(150, 670)
    # Verticales
    crosswalk_y(530, 150)
    crosswalk_y(670, 150)
    
    # Tercera  interseccion
    pygame.draw.rect(window, GREY_ROAD, (930, 150, ROAD_WIDTH+40, ROAD_WIDTH))
    crosswalk_x(550, 130)
    crosswalk_x(550, 270)
    # Verticales
    crosswalk_y(930, 150)
    crosswalk_y(1070, 150)
    
    # Cuarta interseccion
    pygame.draw.rect(window, GREY_ROAD, (130, 550, ROAD_WIDTH+40, ROAD_WIDTH))
    crosswalk_x(550, 530)
    crosswalk_x(550, 670)
    # Verticales
    crosswalk_y(130, 550)
    crosswalk_y(270, 550)
    
    # Quinta interseccion
    pygame.draw.rect(window, GREY_ROAD, (530, 550, ROAD_WIDTH+40, ROAD_WIDTH))
    crosswalk_x(950, 130)
    crosswalk_x(950, 270)
    # Verticales
    crosswalk_y(530, 550)
    crosswalk_y(670, 550)
    
    # Sexta interseccion
    pygame.draw.rect(window, GREY_ROAD, (930, 550, ROAD_WIDTH+40, ROAD_WIDTH))
    crosswalk_x(950, 530)
    crosswalk_x(950, 670)
    # Verticales
    crosswalk_y(930, 550)
    crosswalk_y(1070, 550)   
    
        
        


def main():
    pygame.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        window.fill(GREEN)
        draw_elements()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
