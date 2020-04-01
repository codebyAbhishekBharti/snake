import pygame
import random

pygame.init()
# create snake class
class snake():
    body = []
    def __init__(self):
        self.head = cube(100,100)
        self.body.append(self.head)
        self.body.append(cube(75,100))
        self.body.append(cube(50,100))
    def move(self,dx = 25,dy =0):
        for c in reversed(range(len(self.body))):
            if c == 0:
                if self.body[c].positionx == -25:
                    self.body[c].positionx = 475
                elif self.body[c].positionx == 500:
                    self.body[c].positionx = 0
                elif self.body[c].positiony == 500:
                    self.body[c].positiony = 0
                elif self.body[c].positiony == -25:
                    self.body[c].positiony = 475
                else:
                    self.body[c].positionx += dx
                    self.body[c].positiony += dy
            else:
                self.body[c].positionx = self.body[c-1].positionx
                self.body[c].positiony = self.body[c-1].positiony
            
    def draw_snake(self):
        for c in self.body:
            pygame.draw.rect(window,(255,255,255),(c.positionx+1,c.positiony+1,23,23))
            

class cube():
    def __init__(self,x,y):
        self.positionx = x
        self.positiony = y
    def draw(self):
        pygame.draw.rect(window,(255,255,255),(self.positionx,self.positiony,25,25))

def random_snack(snake):
    global snack,x,y
    snack = True
    rand_x = [i*25 for i in range(20)]
    rand_y = [i*25 for i in range(20)]
    for i in snake.body:
        if i.positionx in rand_x:
            rand_x.remove(i.positionx)
        if i.positiony in rand_y:
            rand_y.remove(i.positiony)
    x = random.choice(rand_x)
    y = random.choice(rand_y)
    




# create screen and grid
width = 500
window = pygame.display.set_mode((width,width))
pygame.display.set_caption('Snake')
rows = 20
clock = pygame.time.Clock()
clock.tick(20)
dx = 25
dy = 0
game = True
snack = False
x=0
y=0
# grid
def grid():
    # size = width/rows
    x= 0
    y=0
    for _ in range(20):
        x += 25
        y += 25
        pygame.draw.line(window,(255,255,255),(x,0),(x,width))
        pygame.draw.line(window,(255,255,255),(0,y),(width,y))

def check_if_snake_ate(snake,x,y):
    global snack
    if (snake.body[0].positionx == x) and (snake.body[0].positiony == y):
        a= snake.body[0].positionx
        b= snake.body[0].positiony
        print('ate')
        if dx == 25:
            a = snake.body[0].positionx-25
        elif dx == -25:
            a = snake.body[0].positionx+25
        elif dy == 25:
            b = snake.body[0].positiony-25
        elif dy == -25:
            b = snake.body[0].positiony+25
        snake.body.insert(1,cube(a,b))
        snack = False
# font for game over
font =  pygame.font.Font('freesansbold.ttf', 30)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
text = font.render('Game Over', True, green) 
textRect = text.get_rect()  
textRect.center = (width // 2, width // 2)


# game loop
hiss = snake()
while True:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT]:
            if dx == 25:
                game = False
            dx = -25
            dy = 0
        elif keys[pygame.K_RIGHT]:
            if dx == -25:
                game = False
            dx = 25
            dy = 0
        elif keys[pygame.K_UP]:
            if dy == 25:
                game = False
            dx = 0
            dy = -25
        elif keys[pygame.K_DOWN]:
            if dy == -25:
                game = False
            dx = 0
            dy = 25

    if game:
        grid()
        hiss.draw_snake()
        hiss.move(dx,dy)
        if snack == False:
            random_snack(hiss)
        pygame.draw.rect(window,(255,0,255),(x,y,25,25))
        check_if_snake_ate(hiss,x,y)
    else:
        window.blit(text,textRect)
    pygame.time.wait(30)
    pygame.display.update()
