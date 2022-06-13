import pygame
import random

WIDTH, HEIGHT = 800, 600

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Game')

# colours
RED, BLUE, YELLOW, GREEN, BLACK, WHITE, GREY = (255, 102, 102), (128, 191, 255), (234, 234, 2), (0, 150, 59), (26, 26, 26), (242, 242, 242), (179, 179, 179)
color = RED

# car dimensions
carW, carL, carX, carY = 40, 100, 390, 420

# obstacles
obstaclesW, obstalcesL = 90, 90
obstaclesX = []
obstaclesY = [] 
obstaclesSpeed = 20

# import images
car = pygame.image.load('images/car.png').convert_alpha()
game = pygame.image.load('images/game.png').convert_alpha()
ttt = pygame.image.load('images/2022.gif').convert_alpha()
easyButton = pygame.image.load('images/easybutton.png').convert_alpha()
hardButton = pygame.image.load('images/hardbutton.png').convert_alpha()
redButton = pygame.image.load('images/red.png')
blueButton = pygame.image.load('images/blue.png')
greenButton = pygame.image.load('images/green.png')

inMenu = True

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        global inMenu
        action = False
        display.blit(self.image, (self.rect.x, self.rect.y))

        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                inMenu = False

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

while inMenu:
    display.fill(BLACK)
    display.blit(car, (20, 30))
    display.blit(game, (250, 10))
    display.blit(ttt, (550, 10))

    easy_button = Button(100, 400, easyButton)
    hard_button = Button(500, 400, hardButton)
    red_button = Button(100, 200, redButton)
    blue_button = Button(300, 200, blueButton)
    green_button = Button(500, 200, greenButton)

    easy_button.draw()
    hard_button.draw()
    red_button.draw()
    blue_button.draw()
    green_button.draw()
   
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

inGame = True
while inGame:
    gameWindow()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and carX >= 261:
        carX -= 1
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and carX <= (WIDTH - 299):
        carX += 1

    pygame.time.delay(2)
    pygame.display.update()
