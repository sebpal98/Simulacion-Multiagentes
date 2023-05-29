import pygame
import random
import time
import threading
from collections import Counter
from scipy.stats import chi2
from datetime import datetime
import GenerateNums

# Dimensiones de la ventana
window_width = 1200
window_height = 800

# Colores
BLACK = (0, 0, 0)
GREEN = (36, 202, 61)
GREY_ROAD = (54, 59, 55)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 105, 0)
BLUE = (135, 206, 235)
RED = (255, 0, 0)
GREEN_LIGHT = (0, 255, 0)

# MODIFICADOR DE COLOR CAJAS DE COLISION
COLLIDER_COLOR = (0, 0, 255, 250)  # Azul transparente

# Dimensiones de las carreteras
ROAD_WIDTH = 120
ROAD_HEIGHT = 30

# Dimensiones de las aceras
sidewalk_width = 20

window = pygame.display.set_mode((window_width, window_height), pygame.SRCALPHA)
pygame.display.set_caption("Simulación de Cruce Vehicular")
clock = pygame.time.Clock()

class Carro:
    def __init__(self, x, y,width, height, color, direction):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.direction = direction

    def move(self):
        if self.direction == 'up':
            self.rect[1] += 2.5
        elif self.direction == 'down':
            self.rect[1] -= 2.5
        elif self.direction == 'left':
            self.rect[0] -= 2.5
        elif self.direction == 'right':
            self.rect[0] += 2.5
            
    def __str__(self):
        return f"Carrito: rect: {self.rect}, color: {self.color}, direction: {self.direction}"
    def check_collision(self, rect):
        return self.rect.colliderect(rect)
class Bus:
    def __init__(self, x, y,width, height, color, direction):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.direction = direction

    def move(self):
        if self.direction == 'up':
            self.rect[1] += 1.5
        elif self.direction == 'down':
            self.rect[1] -= 1.5
        elif self.direction == 'left':
            self.rect[0] -= 1.5
        elif self.direction == 'right':
            self.rect[0] += 1.5
    def __str__(self):
        return f"Bus: rect: {self.rect}, color: {self.color}, direction: {self.direction}"
    def check_collision(self, rect):
        return self.rect.colliderect(rect)
class VehicleGenerator(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.cars = []
        self.lock = threading.Lock()

    def run(self):
        num_cars_per_bus = 0
        while True:
            if num_cars_per_bus < 3:
                self.addCarToCars(self.validateCar(self.generateVehicle()))
                num_cars_per_bus+=1
            else:
                self.addCarToCars(self.validateBus(self.generateBus()))
                print('BUUUUUUUS')
                num_cars_per_bus=0

            for car in self.cars:
                if not self.verifyIsInMap(car):
                    self.deleteCarFromCars(car)
            time.sleep(1.5)

    def addCarToCars(self, car):
            self.lock.acquire()  # Adquirir el bloqueo
            try:
                self.cars.append(car)
            finally:
                self.lock.release()  # Liberar el bloqueo
    def deleteCarFromCars(self, car):
            self.lock.acquire()  # Adquirir el bloqueo
            try:
                self.cars.remove(car)
            finally:
                self.lock.release()  # Liberar el bloqueo
    def validateCar(self,car):
        while car==0:
            car = self.generateVehicle()
        return car
    def validateBus(self,bus):
        while bus==0:
            bus = self.generateBus()
        return bus
    def verifyIsInMap(self, car):
        if car.direction == 'right' and car.rect.x>1190:
            return False
        if car.direction == 'left' and car.rect.x<0:
            return False
        if car.direction == 'up' and car.rect.y>790:
            return False
        if car.direction == 'down' and car.rect.y<0:
            return False
        else:
            return True
    def generateBus(self):
        gen = GenerateNums.get_numbers(350)
        numchoiced = random.choice(gen)
        seed= int(numchoiced*10000* time.time())
        num = self.MonteCarlo(1,seed)
        coordenada = self.getPlaceToSpawnByNum(num[0])
        width=random.choice([35,85])
        height=0
        direction=''
        if width == 85:
            height = 35
            if coordenada[0]==0:
                direction = 'right'
                return Carro(coordenada[0],coordenada[1],width, height, RED, direction)

            if coordenada[0]==1190:
                direction = 'left'
                return Carro(coordenada[0],coordenada[1],width, height, RED, direction)
        else:
            height=85
            if coordenada[1]==0:
                direction='up'
                return Carro(coordenada[0],coordenada[1],width, height, RED, direction)

            if coordenada[1]==790:
                direction='down'
                return Carro(coordenada[0],coordenada[1],width, height, RED, direction)
        return 0
    def generateVehicle(self):
        gen = GenerateNums.get_numbers(350)
        numchoiced = random.choice(gen)
        print(f'NUMERO ELEGIDO: {numchoiced}')
        seed= int(numchoiced*10000* time.time())
        print(f'seed {seed}')
        num = self.MonteCarlo(1,seed)
        print(f'num: {num[0]}')
        coordenada = self.getPlaceToSpawnByNum(num[0])
        width=random.choice([30,50])
        color=random.choice([BLUE,YELLOW, GREEN,ORANGE,WHITE,BLACK])
        height=0
        direction=''
        if width == 50:
            height = 30
            if coordenada[0]==0:
                direction = 'right'
                return Carro(coordenada[0],coordenada[1],width, height, color, direction)

            if coordenada[0]==1190:
                direction = 'left'
                return Carro(coordenada[0],coordenada[1],width, height, color, direction)
        else:
            height=50
            if coordenada[1]==0:
                direction='up'
                return Carro(coordenada[0],coordenada[1],width, height, color, direction)

            if coordenada[1]==790:
                direction='down'
                return Carro(coordenada[0],coordenada[1],width, height, color, direction)
        return 0
    
    def getPlaceToSpawnByNum(self,number):
        if number < 0.1:
            return (0,230)
        elif number < 0.2:
            return (0, 630)
        elif number < 0.3:
            return (1190, 170)
        elif number < 0.4:
            return (1190, 570)
        elif number < 0.5:
            return (160, 0)
        elif number < 0.6:
            return (560, 0)
        elif number < 0.7:
            return (960, 0)
        elif number < 0.8:
            return (220,790)
        elif number < 0.9:
            return (620,790)
        else:
            return (1020,790)

    def MonteCarlo(self,quantity, seed):
        generated_nums = []
        xi = seed
        while quantity > 0:
            x2i = xi * xi
            extension = len(str(x2i))
            quantity -= 1
            extracted = self.extractNums(x2i, extension)
            generated_nums.append(extracted / 10000.0)
            xi = extracted
        return generated_nums

    def extractNums(self,num, extension):
        segmento = 0
        num_str = str(num)
        inicio = (extension - 4) // 2
        fin = inicio + 4
        if len(num_str) >= 4:
            segmento = int(num_str[inicio:fin])
        return segmento

class Traffic_Light:
    LIGHT_COLOR = (255, 0, 0)  # Rojo

    def __init__(self, x_light, y_light, light_size, x_collider, y_collider, collider_size):
        self.color = Traffic_Light.LIGHT_COLOR
        self.light_rect = pygame.Rect(x_light, y_light, light_size[0], light_size[1])
        self.collider_rect = pygame.Rect(x_collider, y_collider, collider_size[0], collider_size[1])

    def change_color(self):
        if self.color == Traffic_Light.LIGHT_COLOR:
            self.color = (0, 255, 0)  # Verde
        else:
            self.color = Traffic_Light.LIGHT_COLOR

    def draw(self, screen):    
        transparent_surface = pygame.Surface((self.collider_rect.width, self.collider_rect.height), pygame.SRCALPHA)
        transparent_surface.fill(COLLIDER_COLOR)
        screen.blit(transparent_surface, self.collider_rect)
        pygame.draw.rect(screen, self.color, self.light_rect)

class Bus_Stop:
    

    def __init__(self, x, y, stop_size, x_collider, y_collider, collider_size):
        self.rect = pygame.Rect(x, y, stop_size[0], stop_size[1])
        self.collider_rect = pygame.Rect(x_collider, y_collider, collider_size[0], collider_size[1])

    def draw(self, screen):

        transparent_surface = pygame.Surface((self.collider_rect.width, self.collider_rect.height), pygame.SRCALPHA)
        transparent_surface.fill(COLLIDER_COLOR)
        screen.blit(transparent_surface, self.collider_rect)
        pygame.draw.rect(screen, ORANGE, self.rect)

def draw_elements():
    roads()
    cross_walks()
    road_stops()
    traffic_lights()

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
    for y in range(40, window_height, 340):
        # Verticales de abajo hacia arriba
        pygame.draw.rect(window, WHITE, (168, y, 5, 30))    
        pygame.draw.polygon(window, WHITE, ([170,y+30],[180,y+25],[170,y+50],[160,y+25]))
        # Verticales de abajo abajo hacia arriba
        pygame.draw.rect(window, WHITE, (228, y+30, 5, 30))    
        pygame.draw.polygon(window, WHITE, ([230,y+30],[240,y+35],[230,y+15],[220,y+35]))
        
        # Dibujar las flechas Verticales
        pygame.draw.rect(window, WHITE, (168+constant_roads, y, 5, 30))    
        pygame.draw.polygon(window, WHITE, ([170+constant_roads,y+30],[180+constant_roads,y+25],[170+constant_roads,y+50],[160+constant_roads,y+25]))
        # Verticales de abajo abajo hacia arriba
        pygame.draw.rect(window, WHITE, (228+constant_roads, y+30, 5, 30))    
        pygame.draw.polygon(window, WHITE, ([230+constant_roads,y+30],[240+constant_roads,y+35],[230+constant_roads,y+15],[220+constant_roads,y+35]))
       
        #Dibujar las flechas Horizontales
        pygame.draw.rect(window, WHITE, (168+constant_roads*2, y, 5, 30))    
        pygame.draw.polygon(window, WHITE, ([170+constant_roads*2,y+30],[180+constant_roads*2,y+25],[170+constant_roads*2,y+50],[160+constant_roads*2,y+25]))
        # Verticales de abajo abajo hacia arriba
        pygame.draw.rect(window, WHITE, (228+constant_roads*2, y+30, 5, 30))    
        pygame.draw.polygon(window, WHITE, ([230+constant_roads*2,y+30],[240+constant_roads*2,y+35],[230+constant_roads*2,y+15],[220+constant_roads*2,y+35]))

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

def road_stops():
    bus_stop1 = Bus_Stop(400,270,(60,20) ,460,230,(5,40))
    bus_stop1.draw(window)
    
    bus_stop2 = Bus_Stop(330,130,(60,20) ,325,150,(5,40))
    bus_stop2.draw(window)
    
    bus_stop3 = Bus_Stop(930,440,(20,60) ,950,500,(40,5))
    bus_stop3.draw(window)
    
    bus_stop4 = Bus_Stop(670,370,(20,60) ,630,370,(40,5))
    bus_stop4.draw(window)
    
    bus_stop5 = Bus_Stop(130,360,(20,60) ,150,420,(40,5))
    bus_stop5.draw(window)
    
    bus_stop6 = Bus_Stop(810,670,(60,20) ,870,630,(5,40))
    bus_stop6.draw(window)
    
    bus_stop7 = Bus_Stop(340,530,(60,20) ,340,550,(5,40))
    bus_stop7.draw(window)

def traffic_lights():
    CONSTANT_Y = 400
    # Semaforos horizontales, en orden de primera carretera y segunda
    for y in range(170, window_width, CONSTANT_Y):
        traffic_light1 = Traffic_Light(y,150,(10,10) , y-30,120,(50,20))
        traffic_light1.draw(window)
        
        traffic_light1 = Traffic_Light(y,150+CONSTANT_Y,(10,10) , y-30,120+CONSTANT_Y,(50,20))
        traffic_light1.draw(window)
        
    # Semaforos horizontales, en orden de primera carretera y segunda
    for y in range(240, window_width, CONSTANT_Y):
        traffic_light1 = Traffic_Light(y,260,(10,10) , y-10,280,(50,20))
        traffic_light1.draw(window)
        
        traffic_light1 = Traffic_Light(y,260+CONSTANT_Y,(10,10) , y-10,280+CONSTANT_Y,(50,20))
        traffic_light1.draw(window)
        
     # Semaforos horizontales, en orden de primera carretera y segunda
    for y in range(260, window_width, CONSTANT_Y):
        traffic_light1 = Traffic_Light(y,170,(10,10) , y+20,140,(20,50))
        traffic_light1.draw(window)
        
        traffic_light1 = Traffic_Light(y,170+CONSTANT_Y,(10,10) , y+20,140+CONSTANT_Y,(20,50))
        traffic_light1.draw(window)
        
    for y in range(150, window_width, CONSTANT_Y):
        traffic_light1 = Traffic_Light(y,240,(10,10) , y-30,230,(20,50))
        traffic_light1.draw(window)
        
        traffic_light1 = Traffic_Light(y,240+CONSTANT_Y,(10,10) , y-30,230+CONSTANT_Y,(20,50))
        traffic_light1.draw(window)
        
def main():
    pygame.init()
    cars=[]
    generator = VehicleGenerator()
    generator.start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        window.fill(GREEN)
        draw_elements()
        cars=generator.cars
        for car in cars:
            pygame.draw.rect(window, car.color, car.rect)
            car.move()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
    