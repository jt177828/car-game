import pygame as pg

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


def gameWindow():
    display.fill(black)

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


game = True
while game:
    pg.event.clear()
    gameWindow()
    # car()

    key = pg.key.get_pressed()

    if (key[pg.K_LEFT] or key[pg.K_a]) and carX >= 261:
        carX -= 1
    if (key[pg.K_RIGHT] or key[pg.K_d]) and carX <= (width - 299):
        carX += 1

    pg.time.delay(2)
    pg.display.update()
