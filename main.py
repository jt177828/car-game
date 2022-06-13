import pygame
import random

WIDTH = 800
HEIGHT = 600

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Game')

# colours
RED = (255, 102, 102)
BLUE = (128, 191, 255)
YELLOW = (230, 184, 0)
GREEN = (0, 150, 59)
BLACK = (26, 26, 26)
WHITE = (242, 242, 242)
GREY = (179, 179, 179)

color = RED

# car dimensions
carW = 40
carL = 100
carX = 390
carY = 420
obstaclesX = 20

# import images
car = pygame.image.load('images/car.png').convert_alpha()
game = pygame.image.load('images/game.png').convert_alpha()
ttt = pygame.image.load('images/2022.gif').convert_alpha()
easyButton = pygame.image.load('images/easybutton.png').convert_alpha()
hardButton = pygame.image.load('images/hardbutton.png').convert_alpha()


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False
        display.blit(self.image, (self.rect.x, self.rect.y))
        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                print("d")


easy_button = Button(100, 400, easyButton)
hard_button = Button(500, 400, hardButton)


def menu():
    display.fill(BLACK)
    display.blit(car, (20, 30))
    display.blit(game, (250, 10))
    display.blit(ttt, (550, 10))

    easy_button.draw()
    hard_button.draw()


def gameWindow():
    display.fill(BLACK)

    pygame.draw.rect(display, GREY, (240, 0, 20, HEIGHT))  # draw left curb
    # draw right curb
    pygame.draw.rect(display, GREY, (WIDTH - 260, 0, 20, HEIGHT))

    for i in range(10):
        pygame.draw.rect(display, YELLOW, ((WIDTH / 2 - 20), 80 *
                                           (i - 1), 20, 40))  # draw lines on the road
        # draw trees on the left
        pygame.draw.rect(display, GREEN, (200, 80 * (i - 1), 30, 30))

        # draw trees on the right
        pygame.draw.rect(display, GREEN, (WIDTH - 220, 80 * (i - 1), 30, 30))

    pygame.draw.rect(display, color, (carX, carY, carW, carL))  # car


inMenu = True
while inMenu:
    # pygame.event.clear()
    menu()

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            inMenu = False

    pygame.display.update()

inGame = True
while inGame:
    gameWindow()
    pygame.draw.rect(display, WHITE, (obstaclesX * 40 + 240, 0, 40, 40))

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and carX >= 261:
        carX -= 1
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and carX <= (WIDTH - 299):
        carX += 1

    pygame.time.delay(2)
    pygame.display.update()
