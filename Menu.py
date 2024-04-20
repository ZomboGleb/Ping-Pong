import pygame
import turtle

pygame.init()
pygame.mixer.init()

back = (85, 85, 85)
mw = pygame.display.set_mode((1540, 810))
mw.fill((back))
clock = pygame.time.Clock()

platform_x1 = 200
platform_y1 = 640

platform_x2 = 200
platform_y2 = +30

dx = 2
dy = 2

move_right1 = False
move_left1 = False

move_right2 = False
move_left2 = False

game_over = False


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width = 10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))

points_Z = 0

points_A = 0

BLACK = (0,0,0)

RED = (255,0,0)

BLUE = (17, 0, 255)

player1_text = Label(600, 720, 50, 50, back)
player1_text.set_text('Player1', 40, RED)
player1_text.draw(20, 20)

player2_text = Label(600, 670, 50, 50, back)
player2_text.set_text('Player2', 40, RED)
player2_text.draw(20, 20)


score_text1 = Label(0, 690, 50, 50, back)
score_text1.set_text('Player1:', 40, BLUE)
score_text1.draw(20, 20)

score1 = Label(190, 713, 50, 40, back)
score1.set_text('0', 40, BLACK)
score1.draw(0, 0)

score_text2 = Label(220, 690, 50, 50, back)
score_text2.set_text('Player2:', 40, BLUE)
score_text2.draw(20, 20)

score2 = Label(410, 713, 50, 40, back)
score2.set_text('0', 40, BLACK)
score2.draw(0, 0)

pygame.mixer.music.load("Fon-music.mp3")
Fon = Picture('image.png', 0, 0, 1540, 650)
ball = Picture('Ball.png', 160, 200, 50, 50)
Platform1 = Picture('platform.png', platform_x1, platform_y1, 99, 25)
Platform2 = Picture('platform.png', platform_x2, platform_y2, 99, 25)
pygame.mixer.music.play()



start_x = 5
start_y = 5
count = 9

while not game_over:
    Fon.fill()
    ball.fill()
    Platform1.fill()
    Platform2.fill()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right1 = True
            if event.key == pygame.K_d:
                move_right2 = True
            if event.key == pygame.K_LEFT:
                move_left1 = True
            if event.key == pygame.K_a:
                move_left2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right1 = False
            if event.key == pygame.K_d:
                move_right2 = False
            if event.key == pygame.K_LEFT:
                move_left1 = False
            if event.key == pygame.K_a:
                move_left2 = False

    if move_right1 and Platform1.rect.x < 1450:
        Platform1.rect.x += 3
    if move_left1 and Platform1.rect.x > 0:
        Platform1.rect.x -= 3

    if move_right2 and Platform2.rect.x < 1450:
        Platform2.rect.x += 3
    if move_left2 and Platform2.rect.x > 0:
        Platform2.rect.x -= 3


    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 1500 or ball.rect.x < 0:
        dx *= -1

    if ball.rect.y > 630:
        time_text = Label(900, 690, 50, 50, back)
        time_text.set_text("Player2 WIN!", 60, (0, 200, 0))
        time_text.draw(10, 10)
        game_over = True
    if ball.rect.y < -0:
        time_text = Label(900, 690, 50, 50, back)
        time_text.set_text("Player1 WIN!", 60, (0, 200, 0))
        time_text.draw(10, 10)
        game_over = True


    if ball.rect.colliderect(Platform1.rect):
        points_Z += 1
        dy *= -1
        score1.set_text(str(points_Z), 40, BLACK)
        score1.draw(0, 0)
    if ball.rect.colliderect(Platform2.rect):
        points_A += 1
        dy *= -1
        score2.set_text(str(points_A), 40, BLACK)
        score2.draw(0, 0)

    Fon.draw()
    Platform1.draw()
    Platform2.draw()
    ball.draw()

    pygame.display.update()

pygame.display.update()
turtle.Screen().mainloop()
clock.tick(40)