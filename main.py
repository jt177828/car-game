import pygame as pg
import random

width = 800
height = 600

pg.init()
display = pg.display.set_mode((width, height))

# colours
red = (255, 102, 102)
blue = (128, 191, 255)
yellow = (230, 184, 0)
green = (0, 150, 59)
black = (26, 26, 26)
white = (242, 242, 242)
grey = (179, 179, 179)

color = red

# car dimensions
carW = 40
carL = 100
carX = 390
carY = 420
obstaclesX = 20

# import images
car = pg.image.load('car.png')
game = pg.image.load('game.png')
ttt = pg.image.load('2022.gif')

count = 0

def menu():
    display.fill(black)
    display.blit(car, (20, 40))
    display.blit(game, (350, 40))
    display.blit(ttt, (600, 40))

    pg.display.update()

def gameWindow():
    display.fill(black)

    obstacles()

    pg.draw.rect(display, grey, (240, 0, 20, height))  # draw left curb
    # draw right curb
    pg.draw.rect(display, grey, (width - 260, 0, 20, height))

    for i in range(10):
        pg.draw.rect(display, yellow, ((width / 2 - 20), 80 *
                     (i - 1), 20, 40))  # draw lines on the road
        # draw trees on the left
        pg.draw.rect(display, green, (200, 80 * (i - 1), 30, 30))
        # draw trees on the right
        pg.draw.rect(display, green, (width - 220, 80 * (i - 1), 30, 30))

    pg.draw.rect(display, color, (carX, carY, carW, carL))  # car

    
    pg.display.update()

def obstacles():
    if count % 8 == 0:
        obstaclesX = random.randint(0, 7)

inMenu = True
while inMenu:
    pg.event.clear()
    menu()

    key = pg.key.get_pressed()
    if key[pg.K_ESCAPE]:
        pg.quit()

inGame = True
while inGame:
    pg.event.clear()
    gameWindow()
    # car()
    obstacles()
    pg.draw.rect(display, white, (obstaclesX * 40 + 240, 0, 40, 40))


    key = pg.key.get_pressed()
    if key[pg.K_ESCAPE]:
        pg.quit()
    if (key[pg.K_LEFT] or key[pg.K_a]) and carX >= 261:
        carX -= 1
    if (key[pg.K_RIGHT] or key[pg.K_d]) and carX <= (width - 299):
        carX += 1

    count += 1

    pg.time.delay(2)
    pg.display.update()
