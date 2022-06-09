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
car = pg.image.load('car.png').convert_alpha()
game = pg.image.load('game.png').convert_alpha()
ttt = pg.image.load('2022.gif').convert_alpha()
button = pg.image.load('button.png').convert_alpha()

count = 0


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.coords = (x, y)

    def draw(self):
        display.blit(self.image, (self.rect.x, self.rect.y))


easyButton = Button(200, 500, button)
hardButton = Button(400, 500, button)


def menu():
    display.fill(black)
    display.blit(car, (20, 30))
    display.blit(game, (250, 10))
    display.blit(ttt, (550, 10))

    easyButton.draw()
    hardButton.draw()

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
