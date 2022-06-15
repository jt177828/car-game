import pygame
import random

WIDTH, HEIGHT = 800, 600

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Game')

# colours
RED, BLUE, YELLOW, GREEN, BLACK, WHITE, GREY = (255, 102, 102), (128, 191, 255), (
    234, 234, 2), (0, 150, 59), (26, 26, 26), (242, 242, 242), (179, 179, 179)
color = RED

# car dimensions
carW, carL, carX, carY, carSpeed = 40, 100, 390, 480, 2

# obstacles
obstaclesW, obstaclesL, obstaclesSpeed = 70, 70, 1
obstaclesX = [-2000]
obstaclesY = [-2000]

# import images
car = pygame.image.load('images/car.png').convert_alpha()
game = pygame.image.load('images/game.png').convert_alpha()
ttt = pygame.image.load('images/2022.gif').convert_alpha()
easyButton = pygame.image.load('images/easybutton.png').convert_alpha()
hardButton = pygame.image.load('images/hardbutton.png').convert_alpha()
gameOver = pygame.image.load('images/gameover.png').convert_alpha()

#  font for text
font = pygame.font.SysFont('freesansbold.ttf', 60)

inMenu = True  # variable used in the class


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
                action = True

        return action


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


while inMenu:
    display.fill(BLACK)
    display.blit(car, (20, 30))
    display.blit(game, (250, 10))
    display.blit(ttt, (550, 10))

    easy_button = Button(100, 400, easyButton)
    hard_button = Button(500, 400, hardButton)

    if easy_button.draw() == True:
        inMenu = False
        speed = 800
        obstaclesSpeed = 1
    if hard_button.draw() == True:
        inMenu = False
        speed = 400
        obstaclesSpeed = 2

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

preGame = True
while preGame:
    gameWindow()
    rectCar = pygame.draw.rect(display, color, (carX, carY, carW, carL))  # car
    pygame.display.update()
    pygame.time.wait(3000)

    preGame = False

inGame = True

count = 0
score = 0
while inGame:
    gameWindow()
    rectCar = pygame.draw.rect(display, color, (carX, carY, carW, carL))  # car

    for i in range(len(obstaclesX)):
        rectObstacles = pygame.draw.rect(
            display, WHITE, (obstaclesX[i], obstaclesY[i], obstaclesW, obstaclesL))

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if count % speed == 0:
        obstaclesX.append(random.randint(0, 3) * 70 + 260)
        obstaclesY.append(0)

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and carX >= 261:
        carX -= carSpeed
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and carX <= (WIDTH - 299):
        carX += carSpeed

    scoreDisplay = font.render(f"Score: {str(score)}", 1, WHITE)
    display.blit(scoreDisplay, (20, 20))

    for i in reversed(range(len(obstaclesX))):
        obstaclesY[i] += obstaclesSpeed
        if obstaclesY[i] > 600:
            obstaclesX.pop(i)
            obstaclesY.pop(i)
            score += 1

    if pygame.Rect.colliderect(rectCar, rectObstacles):
        inGame = False

    count += 1

    pygame.time.delay(2)
    pygame.display.update()

endScreen = True
while endScreen:
    display.blit(gameOver, (100, 200))
    scoreDisplay = font.render(f"Final Score: {str(score)}", 1, WHITE)
    display.blit(scoreDisplay, (400, 400))

    pygame.display.update()
